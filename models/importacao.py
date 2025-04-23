from pydantic import BaseModel, Field
from typing import Dict, Optional

class DadoAnualImportacao(BaseModel):
    quantidade: Optional[int] = Field(None, example=42661, description="Quantidade importada")
    valor: Optional[int] = Field(None, example=99201, description="Valor em reais da importação")

class Importacao(BaseModel):
    id: int = Field(..., example=1, description="ID do registro")
    pais: str = Field(..., example="África do Sul", description="Nome do país de origem")
    historico: Dict[str, DadoAnualImportacao] = Field(
        ..., 
        description="Valores por ano, com quantidade e valor"
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