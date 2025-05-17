# models/comercializacao.py
from typing import List
from pydantic import BaseModel, Field

class ItemComercializacao(BaseModel):
    produto: str = Field(..., example="VINHO DE MESA", description="Nome do produto comercializado")
    quantidade: int = Field(..., example=187016848, description="Quantidade comercializada (em litros)")
    sub_items: List["ItemComercializacao"] = Field(default_factory=list, description="Detalhamento por tipo")

    class Config:
        json_schema_extra = {
            "example": {
                "produto": "VINHO DE MESA",
                "quantidade": 187016848,
                "sub_items": [
                    {"produto": "Tinto", "quantidade": 165097539, "sub_items": []},
                    {"produto": "Rosado", "quantidade": 2520748, "sub_items": []},
                    {"produto": "Branco", "quantidade": 19398561, "sub_items": []}
                ]
            }
        }

# Corrige referência recursiva
ItemComercializacao.update_forward_refs()