from pydantic import BaseModel, Field
from typing import Dict

from pydantic import BaseModel, Field
from typing import Optional

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