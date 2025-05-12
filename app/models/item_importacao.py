# models/importacao.py
from pydantic import BaseModel, Field
from typing import Optional

class ItemImportacao(BaseModel):
    pais: str = Field(..., example="Argentina", description="País de origem da importação")
    quantidade_kg: Optional[int] = Field(None, example=26272478, description="Quantidade importada em kg")
    valor_usd: Optional[int] = Field(None, example=93869579, description="Valor importado em dólares americanos")

    class Config:
        json_schema_extra = {
            "example": {
                "pais": "Argentina",
                "quantidade": 26272478,
                "valor": 93869579
            }
        }
