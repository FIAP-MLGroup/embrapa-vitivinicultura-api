from typing import List
from pydantic import BaseModel, Field
from pydantic import ConfigDict

class ItemProcessamento(BaseModel):
    produto: str = Field(..., example="TINTAS", description="Nome da cultivar ou grupo")
    quantidade: int = Field(..., example=35881118, description="Quantidade processada em Kg")
    sub_items: List["ItemProcessamento"] = Field(default_factory=list, description="Detalhamento por cultivar")

    class Config:
        json_schema_extra = {
            "example": {
                "produto": "TINTAS",
                "quantidade": 35881118,
                "sub_items": [
                    {"produto": "Alicante Bouschet", "quantidade": 4108858, "sub_items": []},
                    {"produto": "Ancelota", "quantidade": 783688, "sub_items": []}
                ]
            }
        }

# Corrige referência recursiva
ItemProcessamento.update_forward_refs()