from fastapi import APIRouter
from typing import List
from models.producao import Producao, DadoAnualProducao
from core.data_loader import carregar_dados
from core.data_loader import URL

import pandas as pd

router = APIRouter()

@router.get("/producao", 
        response_model=List[Producao],
        summary="Obter dados de produção",
        description="Retorna os dados de produção com base no tipo especificado.",
        tags=["Produção"])
def get_producao():

    df = carregar_dados(URL.PRODUCAO)

    dados = []
    anos = [col for col in df.columns if col.isdigit()]

    for _, row in df.iterrows():
        producao = Producao(
            id=row["id"],
            control=row["control"] if pd.notna(row["control"]) else "",
            produto=row["produto"] if pd.notna(row["produto"]) else "",
            historico={str(ano): 
                DadoAnualProducao(
                    quantidade=int(row[str(ano)])
                ) for ano in anos if str(row[str(ano)]).isdigit()}
        )
        dados.append(producao)

    return dados