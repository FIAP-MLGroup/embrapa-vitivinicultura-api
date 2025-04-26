from fastapi import APIRouter
from typing import List
from app.models.comercializacao import Comercializacao
from app.core.data_loader import carregar_dados, URL

router = APIRouter()

@router.get("/comercializacao", 
        response_model=List[Comercializacao],
        summary="Obter dados de comercialização",
        description="Retorna os dados de comercialização com base no tipo especificado.",
        tags=["Comercialização"])
def get_comercializacao():

    df = carregar_dados(URL.COMERCIALIZACAO)

    dados = []
    for _, row in df.iterrows():
        dados.append(
            Comercializacao.from_dataframe_row(row=row, field_map={
                "id": "id",
                "control": "control",
                "produto": "Produto",
                "historico": [col for col in df.columns if col.isdigit()]
            })
        )

    return dados