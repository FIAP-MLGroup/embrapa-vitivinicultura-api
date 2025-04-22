from fastapi import APIRouter
from typing import Dict, List
from models.producao import Producao
from core.data_loader import carregar_dados
from core.data_loader import URL

import pandas as pd

router = APIRouter()

@router.get("/producao", 
        response_model=List[Producao])
def get_producao():

    df = carregar_dados(URL.PRODUCAO)

    dados = []
    anos = [col for col in df.columns if col.isdigit()]

    for _, row in df.iterrows():
        producao = Producao(
            id=row["id"],
            control=row["control"],
            produto=row["produto"],
            series={
                str(ano): int(row[str(ano)]) for ano in anos
            }
        )
        dados.append(producao)

    return dados