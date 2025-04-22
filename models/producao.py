from pydantic import BaseModel, Field
from typing import Dict

class Producao(BaseModel):
    id: int = Field(..., example=1)
    control: str = Field(..., example="VINHO DE MESA")
    produto: str = Field(..., example="VINHO DE MESA")
    series: Dict[str, int] = Field(..., example={"1970": 217208604, "1971": 154264651, "1972": 146953297})

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "control": "VINHO DE MESA",
                "produto": "VINHO DE MESA",
                "series": {
                    "1970": 217208604,
                    "1971": 154264651,
                    "1972": 146953297,
                }
            }
        }