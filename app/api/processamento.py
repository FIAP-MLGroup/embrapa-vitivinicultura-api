from fastapi import APIRouter, Query, HTTPException, Depends
from typing import List
from app.models.item_processamento import ItemProcessamento
from app.core.data_loader import URL
from datetime import datetime
from app.core.security import get_current_user
from app.core.processamento_scraper import ProcessamentoScraper


router = APIRouter()

@router.get(
    "/processamento",
    response_model=List[ItemProcessamento],
    summary="Obter dados de processamento",
    description="Retorna os dados de processamento com base no tipo especificado.",
    tags=["Processamento"],
    dependencies=[Depends(get_current_user)]
)
def get_processamento(
    tipo: str = Query(
        ...,
        description="Tipo de processamento a ser retornado",
        enum=["vinifernas", "americanas_hibridas", "uvas_mesa", "sem_classificacao"],
    ),
    ano: int = Query(..., ge=1970, le=datetime.now().year, description="Ano de processamento a ser consultado (entre 1970 e o ano atual)")
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
    
    return ProcessamentoScraper(url=url_map[tipo], year=ano).get_data()
