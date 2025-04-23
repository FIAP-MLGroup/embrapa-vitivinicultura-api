from fastapi import APIRouter
from typing import List
from models.importacao import Importacao, DadoAnualImportacao
from core.data_loader import carregar_dados
from core.data_loader import URL

import pandas as pd

from fastapi import Query
from fastapi import HTTPException

router = APIRouter()

@router.get(
    "/importacao",
    response_model=List[Importacao],
    summary="Obter dados de importação",
    description="Retorna os dados de importação com base no tipo especificado.",
    tags=["Importação"]
)
def get_importacao(
    tipo: str = Query(
        ...,
        description="Tipo de importacao a ser retornado",
        enum=["vinhos_mesa", "espumantes", "uvas_frescas", "uvas_passas", "suco_uva"],
    )
):
    url_map = {
        "vinhos_mesa": URL.IMPORTACAO_VINHOS_MESA,
        "espumantes": URL.IMPORTACAO_ESPUMANTES,
        "uvas_frescas": URL.IMPORTACAO_UVAS_FRESCAS,
        "uvas_passas": URL.IMPORTACAO_UVAS_PASSAS, 
        "suco_uva": URL.IMPORTACAO_SUCO_UVA,
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

            historico[str(ano)] = DadoAnualImportacao(
                quantidade=int(quantidade) if pd.notna(quantidade) else None,
                valor=int(valor) if pd.notna(valor) else None
            )

        importacao = Importacao(
            id=int(row["Id"]),
            pais=row["País"] if pd.notna(row["País"]) else "",
            historico=historico
        )

        dados.append(importacao)

    return dados