from fastapi import APIRouter
from typing import List
from models.processamento import Processamento, DadoAnualProcessamento
from core.data_loader import carregar_dados
from core.data_loader import URL

import pandas as pd

from fastapi import Query
from fastapi import HTTPException

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
    anos = [col for col in df.columns if col.isdigit()]

    for _, row in df.iterrows():
        processamento = Processamento(
            id=row["id"],
            control=row["control"] if pd.notna(row["control"]) else "",
            cultivar=row["cultivar"] if pd.notna(row["cultivar"]) else "",
            historico={str(ano): 
                DadoAnualProcessamento(
                    quantidade=int(row[str(ano)])
                ) for ano in anos if str(row[str(ano)]).isdigit()}
        )
        dados.append(processamento)

    return dados