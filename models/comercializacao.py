from pydantic import BaseModel, Field
from typing import Dict, Optional

class DadoAnualComercializacao(BaseModel):
    quantidade: Optional[int] = Field(None, example=42661, description="Quantidade comercializada")

class Comercializacao(BaseModel):
    id: int = Field(..., example=1)
    produto: str = Field(..., example="VINHO DE MESA")
    control: Optional[str] = Field("", example="VINHO DE MESA")
    historico: Dict[str, DadoAnualComercializacao] = Field(
        ...,
        example={
            "1970": {"quantidade": 98327606},
            "1971": {"quantidade": 114399031},
            "1972": {"quantidade": 118377367}
        },
    )

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "control": "VINHO DE MESA",
                "produto": "VINHO DE MESA",
                "historico": {
                    "1970": {"quantidade": 98327606},
                    "1971": {"quantidade": 114399031},
                    "1972": {"quantidade": 118377367},
                },
            }
        }