"""
main.py

This module initializes and configures a FastAPI application for the VitiviniculturaApp. 
The application provides an API for querying viticulture data made available by EMBRAPA.

Attributes:
    app (FastAPI): The FastAPI application instance configured with metadata and routes.

Routes:
    - /api/v1/producao: Endpoints related to production data.
    - /api/v1/processamento: Endpoints related to processing data.
    - /api/v1/comercializacao: Endpoints related to commercialization data.
    - /api/v1/importacao: Endpoints related to import data.
    - /api/v1/exportacao: Endpoints related to export data.

Metadata:
    - title: "VitiviniculturaApp"
    - description: "API para consulta dos dados de vitivinicultura disponibilizados pela EMBRAPA"
    - summary: "Tech Challenge da Pós Graduação de Machine Learning da FIAP (5MLET)"
    - version: "0.0.1"
    - license_info: Apache 2.0 License
"""
from fastapi import FastAPI
from app.api import producao
from app.api import processamento
from app.api import comercializacao
from app.api import importacao
from app.api import exportacao

app = FastAPI(
    title="VitiviniculturaApp",
    description="API para consulta dos dados de vitivinicultura disponibilizados pela EMBRAPA",
    summary="Tech Challenge da Pós Graduação de Machine Learning da FIAP (5MLET)",
    version="0.0.1",
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    }
)

app.include_router(producao.router, prefix="/api/v1")
app.include_router(processamento.router, prefix="/api/v1")
app.include_router(comercializacao.router, prefix="/api/v1")
app.include_router(importacao.router, prefix="/api/v1")
app.include_router(exportacao.router, prefix="/api/v1")
