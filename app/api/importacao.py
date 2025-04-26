from fastapi import APIRouter, Query, HTTPException
from typing import List
from app.models.importacao import Importacao
from app.core.data_loader import carregar_dados, URL

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

    for _, row in df.iterrows():
        dados.append(
            Importacao.from_dataframe_row(row=row, field_map={
                "id": "Id",
                "pais": "País",
                "historico": colunas_anos
            })
        )

    return dados