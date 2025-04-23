from pydantic import BaseModel, Field
from typing import Dict, Optional

import pandas as pd

class DadoAnualExportacao(BaseModel):
    quantidade: Optional[int] = Field(None, example=42661, description="Quantidade exportada")
    valor: Optional[int] = Field(None, example=99201, description="Valor em reais da exportação")

class Exportacao(BaseModel):
    id: int = Field(..., example=1, description="ID do registro")
    pais: str = Field(..., example="África do Sul", description="Nome do país de destino")
    historico: Dict[str, DadoAnualExportacao] = Field(
        ..., 
        description="Valores por ano, com quantidade e valor"
    )

    @classmethod
    def from_dataframe_row(cls, row, field_map):

        historico = {}

        anos = sorted({field_map["historico"][i] for i in range(0, len(field_map["historico"]), 2)})

        for i, ano in enumerate(anos):

            col_qtd = field_map["historico"][2 * i]
            col_val = field_map["historico"][2 * i + 1]

            quantidade = row[col_qtd]
            valor = row[col_val]

            if pd.isna(quantidade) and pd.isna(valor):
                continue

            historico[str(ano)] = DadoAnualExportacao(
                quantidade=int(quantidade) if pd.notna(quantidade) else None,
                valor=int(valor) if pd.notna(valor) else None
            )

        return cls(
            id=row[field_map["id"]],
            pais=row[field_map["pais"]] if pd.notna(row[field_map["pais"]]) else "",
            historico=historico
        )

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "pais": "África do Sul",
                "historico": {
                    "2000": {"quantidade": 42661, "valor": 99201},
                    "2001": {"quantidade": 32194, "valor": 106317},
                    "2002": {"quantidade": 157239, "valor": 305701}
                }
            }
        }