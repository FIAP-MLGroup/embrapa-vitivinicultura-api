# models/exportacao.py
from pydantic import BaseModel, Field
from typing import Optional

class ItemExportacao(BaseModel):
    pais: str = Field(..., example="Argentina", description="País de destino da exportação")
    quantidade_kg: Optional[int] = Field(None, example=21015, description="Quantidade exportada em kg")
    valor_usd: Optional[int] = Field(None, example=167696, description="Valor exportado em dólares americanos")

    class Config:
        json_schema_extra = {
            "example": {
                "pais": "Argentina",
                "quantidade": 21015,
                "valor": 167696
            }
        }
