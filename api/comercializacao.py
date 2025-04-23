from fastapi import APIRouter
from typing import List
from models.comercializacao import Comercializacao, DadoAnualComercializacao
from core.data_loader import carregar_dados
from core.data_loader import URL

import pandas as pd

router = APIRouter()

@router.get("/comercializacao", 
        response_model=List[Comercializacao],
        summary="Obter dados de comercialização",
        description="Retorna os dados de comercialização com base no tipo especificado.",
        tags=["Comercialização"])
def get_comercializacao():

    df = carregar_dados(URL.COMERCIALIZACAO)

    dados = []
    anos = [col for col in df.columns if col.isdigit()]

    for _, row in df.iterrows():
        comercializacao = Comercializacao(
            id=row["id"],
            control=row["control"] if pd.notna(row["control"]) else "",
            produto=row["Produto"] if pd.notna(row["Produto"]) else "",
            historico={str(ano): 
                DadoAnualComercializacao(
                    quantidade=int(row[str(ano)])
                ) for ano in anos if str(row[str(ano)]).isdigit()}
        )
        dados.append(comercializacao)

    return dados