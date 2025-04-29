from fastapi import APIRouter, Query, HTTPException, Depends
from typing import List
from app.models.exportacao import Exportacao
from app.core.data_loader import carregar_dados, URL
from app.core.security import get_current_user

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

    for _, row in df.iterrows():
        dados.append(
            Exportacao.from_dataframe_row(row=row, field_map={
                "id": "Id",
                "pais": "País",
                "historico": colunas_anos
            })
        )

    return dados

@router.get(
    "/exportacao-autenticado",
    response_model=List[Exportacao],
    summary="Obter dados de exportação de forma autenticada",
    description="Retorna os dados de exportação com base no tipo especificado.",
    tags=["Exportação"],
    dependencies=[Depends(get_current_user)]
)
def get_exportacao_autenticado(
    tipo: str = Query(
        ...,
        description="Tipo de exportação a ser retornado",
        enum=["vinhos_mesa", "espumantes", "uvas_frescas", "suco_uva"],
    )
):
    return get_exportacao(tipo)