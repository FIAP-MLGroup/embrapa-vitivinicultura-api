# Trabalho Pós Graduação - FIAP 5MLET

Extração dos dados de vitivinicultura fornecidos no site da EMBRAPA

## Bootstrap

Para inicialização deste projeto, os seguintes comando devem ser executados:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install  --requirement requirements.txt
```

## Startup

Para execução da aplicação, o seguinte comando deve ser executado

```bash
uvicorn main:app --reload
```

A API será disponibilizada localmente no endereço http://localhost:8000/

A documentação OpenAPI poderá ser acessada no endereço http://localhost:8000/docs