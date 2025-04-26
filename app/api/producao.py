from fastapi import APIRouter
from typing import List
from app.models.producao import Producao
from app.core.data_loader import carregar_dados, URL

router = APIRouter()

@router.get("/producao", 
        response_model=List[Producao],
        summary="Obter dados de produção",
        description="Retorna os dados de produção com base no tipo especificado.",
        tags=["Produção"])
def get_producao():

    df = carregar_dados(URL.PRODUCAO)

    dados = []
    for _, row in df.iterrows():
        dados.append(
            Producao.from_dataframe_row(row=row, field_map={
                "id": "id",
                "control": "control",
                "produto": "produto",
                "historico": [col for col in df.columns if col.isdigit()]
            })
        )
    return dados