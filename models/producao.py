from pydantic import BaseModel, Field
from typing import Dict, Optional

import pandas as pd

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

    @classmethod
    def from_dataframe_row(cls, row, field_map):
        historico={str(ano): 
            DadoAnualProducao(
                quantidade=int(row[str(ano)])
            ) for ano in field_map["historico"] if str(row[str(ano)]).isdigit()}
        
        return cls(
            id=row[field_map["id"]],
            control=row[field_map["control"]] if pd.notna(row[field_map["control"]]) else "",
            produto=row[field_map["produto"]] if pd.notna(row[field_map["produto"]]) else "",
            historico=historico
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