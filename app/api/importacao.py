from fastapi import APIRouter, Query, HTTPException, Depends
from typing import List
from app.models.item_importacao import ItemImportacao
from app.core.data_loader import URL
from app.core.security import get_current_user
from app.core.importacao_scraper import ImportacaoScraper
from datetime import datetime

router = APIRouter()

@router.get(
    "/importacao",
    response_model=List[ItemImportacao],
    summary="Obter dados de importação",
    description="Retorna os dados de importação com base no tipo especificado.",
    tags=["Importação"],
    dependencies=[Depends(get_current_user)]
)
def get_importacao(
    tipo: str = Query(
        ...,
        description="Tipo de importacao a ser retornado",
        enum=["vinhos_mesa", "espumantes", "uvas_frescas", "uvas_passas", "suco_uva"],
    ),
    ano: int = Query(..., ge=1970, le=datetime.now().year, description="Ano de importação a ser consultado (entre 1970 e o ano atual)")
):
    url_map = {
        "vinhos_mesa": URL.IMPORTACAO_VINHOS_MESA,
        "espumantes": URL.IMPORTACAO_ESPUMANTES,
        "uvas_frescas": URL.IMPORTACAO_UVAS_FRESCAS,
        "uvas_passas": URL.IMPORTACAO_UVAS_PASSAS, 
        "suco_uva": URL.IMPORTACAO_SUCO_UVA,
    }

    if tipo not in url_map:
        raise HTTPException(
            status_code=400,
            detail=f"Tipo '{tipo}' não é válido. Valores esperados: {list(url_map.keys())}",
        )

    return ImportacaoScraper(url=url_map[tipo], year=ano).get_data()
