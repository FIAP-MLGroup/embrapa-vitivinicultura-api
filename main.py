from fastapi import FastAPI
from api import producao
from api import processamento

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