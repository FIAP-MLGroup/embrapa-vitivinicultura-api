from pydantic import BaseModel, Field
from typing import Dict, Optional

import pandas as pd

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

    @classmethod
    def from_dataframe_row(cls, row, field_map):
        historico={str(ano): 
            DadoAnualProcessamento(
                quantidade=int(row[str(ano)])
            ) for ano in field_map["historico"] if str(row[str(ano)]).isdigit()}
        
        return cls(
            id=row[field_map["id"]],
            control=row[field_map["control"]] if pd.notna(row[field_map["control"]]) else "",
            cultivar=row[field_map["cultivar"]] if pd.notna(row[field_map["cultivar"]]) else "",
            historico=historico
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