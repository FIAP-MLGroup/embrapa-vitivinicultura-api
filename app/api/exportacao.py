from fastapi import APIRouter, Query, HTTPException, Depends
from typing import List
from app.models.item_exportacao import ItemExportacao
from app.core.data_loader import URL
from app.core.security import get_current_user
from app.core.importacao_scraper import scrap_data
from datetime import datetime

router = APIRouter()

@router.get(
    "/exportacao",
    response_model=List[ItemExportacao],
    summary="Obter dados de exportação",
    description="Retorna os dados de exportação com base no tipo especificado.",
    tags=["Exportação"],
    dependencies=[Depends(get_current_user)]
)
def get_exportacao(
    tipo: str = Query(
        ...,
        description="Tipo de exportação a ser retornado",
        enum=["vinhos_mesa", "espumantes", "uvas_frescas", "suco_uva"],
    ),
    ano: int = Query(..., ge=1970, le=datetime.now().year, description="Ano de exportação a ser consultado (entre 1970 e o ano atual)")
):
    url_map = {
        "vinhos_mesa": URL.EXPORTACAO_VINHOS_MESA,
        "espumantes": URL.EXPORTACAO_ESPUMANTES,
        "uvas_frescas": URL.EXPORTACAO_UVAS_FRESCAS,
        "suco_uva": URL.EXPORTACAO_SUCO_UVA,
    }

    if tipo not in url_map:
        raise HTTPException(
            status_code=400,
            detail=f"Tipo '{tipo}' não é válido. Valores esperados: {list(url_map.keys())}",
        )
    
    return scrap_data(url=url_map[tipo], year=ano)
