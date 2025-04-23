from fastapi import APIRouter
from typing import List
from models.exportacao import Exportacao, DadoAnualExportacao
from core.data_loader import carregar_dados
from core.data_loader import URL

import pandas as pd

from fastapi import Query
from fastapi import HTTPException

router = APIRouter()

@router.get(
    "/exportacao",
    response_model=List[Exportacao],
    summary="Obter dados de exportação",
    description="Retorna os dados de exportação com base no tipo especificado.",
    tags=["Exportação"]
)
def get_exportacao(
    tipo: str = Query(
        ...,
        description="Tipo de exportação a ser retornado",
        enum=["vinhos_mesa", "espumantes", "uvas_frescas", "suco_uva"],
    )
):
    url_map = {
        "vinhos_mesa": URL.EXPORTACAO_VINHOS_MESA,
        "espumantes": URL.EXPORTACAO_ESPUMANTES,
        "uvas_frescas": URL.EXPORTACAO_UVAS_FRESCAS,
        "suco_uva": URL.EXPORTACAO_SUCO_UVA,
    }

    if tipo not in url_map:
        raise HTTPException(
            status_code=400,
            detail=f"Tipo '{tipo}' não é válido. Valores esperados: {list(url_map.keys())}",
        )

    df = carregar_dados(url_map[tipo])
    dados = []

    # Identifica pares de colunas de anos (quantidade e valor)
    colunas_anos = df.columns[2:]  # Ignora "id" e "País"
    anos = sorted({colunas_anos[i] for i in range(0, len(colunas_anos), 2)})

    for _, row in df.iterrows():
        historico = {}

        for i, ano in enumerate(anos):
            col_qtd = colunas_anos[2 * i]
            col_val = colunas_anos[2 * i + 1]

            quantidade = row[col_qtd]
            valor = row[col_val]

            if pd.isna(quantidade) and pd.isna(valor):
                continue

            historico[str(ano)] = DadoAnualExportacao(
                quantidade=int(quantidade) if pd.notna(quantidade) else None,
                valor=int(valor) if pd.notna(valor) else None
            )

        exportacao = Exportacao(
            id=int(row["Id"]),
            pais=row["País"] if pd.notna(row["País"]) else "",
            historico=historico
        )

        dados.append(exportacao)

    return dados