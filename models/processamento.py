from pydantic import BaseModel, Field
from typing import Dict, Optional

class Processamento(BaseModel):
    id: int = Field(..., example=1)
    control: str = Field(..., example="TINTAS")
    cultivar: str = Field(..., example="TINTAS")
    series: Dict[str, Optional[int]] = Field(
        ..., 
        example={
            "1970": 10448228,
            "1971": 11012833,
            "1972": 10798824
        }
    )

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "control": "TINTAS",
                "cultivar": "TINTAS",
                "series": {
                    "1970": 10448228,
                    "1971": 11012833,
                    "1972": 10798824
                }
            }
        }