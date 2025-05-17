from fastapi import APIRouter, Query, Depends
from typing import List
from app.models.item_comercializacao import ItemComercializacao
from app.core.data_loader import URL
from app.core.security import get_current_user
from app.core.comercializacao_scraper import ComercializacaoScraper
from datetime import datetime

router = APIRouter()

@router.get("/comercializacao", 
        response_model=List[ItemComercializacao],
        summary="Obter dados de comercialização",
        description="Retorna os dados de comercialização com base no tipo especificado.",
        tags=["Comercialização"],
        dependencies=[Depends(get_current_user)])
def get_comercializacao(ano: int = Query(..., ge=1970, le=datetime.now().year, description="Ano da comercialização a ser consultada (entre 1970 e o ano atual)")):

        return ComercializacaoScraper(url=URL.COMERCIALIZACAO, year=ano).get_data()
