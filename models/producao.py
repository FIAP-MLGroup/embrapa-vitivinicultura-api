from pydantic import BaseModel, Field
from typing import Dict, Optional

class DadoAnualProducao(BaseModel):
    quantidade: Optional[int] = Field(None, example=42661, description="Quantidade produzida")

class Producao(BaseModel):
    id: int = Field(..., example=1)
    control: str = Field(..., example="VINHO DE MESA")
    produto: str = Field(..., example="VINHO DE MESA")
    historico: Dict[str, DadoAnualProducao] = Field(
        ..., 
        example={
            "1970": {"quantidade": 217208604}, 
            "1971": {"quantidade": 154264651}, 
            "1972": {"quantidade": 146953297}
        }
    )

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "control": "VINHO DE MESA",
                "produto": "VINHO DE MESA",
                "historico": {
                    "1970": {"quantidade": 217208604},
                    "1971": {"quantidade": 154264651},
                    "1972": {"quantidade": 146953297},
                }
            }
        }