from pydantic import BaseModel, Field
from typing import Dict, Optional

class DadoAnualProcessamento(BaseModel):
    quantidade: Optional[int] = Field(None, example=42661, description="Quantidade processada")

class Processamento(BaseModel):
    id: int = Field(..., example=1)
    control: str = Field(..., example="TINTAS")
    cultivar: str = Field(..., example="TINTAS")
    historico: Dict[str, Optional[DadoAnualProcessamento]] = Field(
        ..., 
        example={
            "1970": {"quantidade": 10448228},
            "1971": {"quantidade": 11012833},
            "1972": {"quantidade": 10798824}
        }
    )

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "control": "TINTAS",
                "cultivar": "TINTAS",
                "historico": {
                    "1970": {"quantidade": 10448228},
                    "1971": {"quantidade": 11012833},
                    "1972": {"quantidade": 10798824}
                }
            }
        }