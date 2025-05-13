from fastapi import APIRouter, Query, Depends
from typing import List
from app.models.item_producao import ItemProducao
from app.core.data_loader import URL
from app.core.security import get_current_user
from datetime import datetime
from app.core.producao_scraper import ProducaoScraper

router = APIRouter()

@router.get("/producao", 
        response_model=List[ItemProducao],
        summary="Obter dados de produção",
        description="Retorna os dados de produção com base no tipo especificado.",
        tags=["Produção"],
        dependencies=[Depends(get_current_user)])
def get_producao(ano: int = Query(..., ge=1970, le=datetime.now().year, description="Ano da produção a ser consultada (entre 1970 e o ano atual)")):

        return ProducaoScraper(url=URL.PRODUCAO, year=ano).get_data()