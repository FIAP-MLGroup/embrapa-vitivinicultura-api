from typing import List
from pydantic import BaseModel, Field

class ItemProducao(BaseModel):
    produto: str = Field(..., example="VINHO DE MESA", description="Nome do produto principal ou subitem.")
    quantidade: int = Field(..., example=169762429, description="Quantidade produzida em litros.")
    sub_items: List['ItemProducao'] = Field(
        default_factory=list,
        description="Lista de subprodutos associados a esse produto.",
        example=[
            {
                "produto": "Tinto",
                "quantidade": 139320884,
                "sub_items": []
            },
            {
                "produto": "Branco",
                "quantidade": 27910299,
                "sub_items": []
            }
        ]
    )

    class Config:
        json_schema_extra = {
            "example": {
                "produto": "VINHO DE MESA",
                "quantidade": 169762429,
                "sub_items": [
                    {
                        "produto": "Tinto",
                        "quantidade": 139320884,
                        "sub_items": []
                    },
                    {
                        "produto": "Branco",
                        "quantidade": 27910299,
                        "sub_items": []
                    }
                ]
            }
        }

# Corrige referência recursiva
ItemProducao.update_forward_refs()