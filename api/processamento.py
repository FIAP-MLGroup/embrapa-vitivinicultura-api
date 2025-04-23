from fastapi import APIRouter, Query, HTTPException
from typing import List
from models.processamento import Processamento
from core.data_loader import carregar_dados, URL

router = APIRouter()

@router.get(
    "/processamento",
    response_model=List[Processamento],
    summary="Obter dados de processamento",
    description="Retorna os dados de processamento com base no tipo especificado.",
    tags=["Processamento"],
)
def get_processamento(
    tipo: str = Query(
        ...,
        description="Tipo de processamento a ser retornado",
        enum=["vinifernas", "americanas_hibridas", "uvas_mesa", "sem_classificacao"],
    )
):
    url_map = {
        "vinifernas": URL.PROCESSAMENTO_VINIFERAS,
        "americanas_hibridas": URL.PROCESSAMENTO_AMERICANAS_HIBRIDAS,
        "uvas_mesa": URL.PROCESSAMENTO_UVAS_MESA,
        "sem_classificacao": URL.PROCESSAMENTO_SEM_CLASSIFICACAO,
    }

    if tipo not in url_map:
        raise HTTPException(
            status_code=400,
            detail=f"Tipo '{tipo}' não é válido. Valores esperados: {list(url_map.keys())}",
        )

    df = carregar_dados(url_map[tipo])

    dados = []
    for _, row in df.iterrows():
        dados.append(
            Processamento.from_dataframe_row(row=row, field_map={
                "id": "id",
                "control": "control",
                "cultivar": "cultivar",
                "historico": [col for col in df.columns if col.isdigit()]
            })
        )

    return dados