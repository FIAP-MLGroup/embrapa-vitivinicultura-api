# Trabalho Pós Graduação - FIAP 5MLET

Extração dos dados de vitivinicultura fornecidos no site da EMBRAPA

## Bootstrap

Para inicialização deste projeto, os seguintes comandos devem ser executados:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Startup

Para inicialização do web server, o seguinte comando deve ser executado:

```bash
uvicorn app.main:app --no-server-header --reload
```

A API será disponibilizada localmente no endereço http://localhost:8000/

A documentação OpenAPI poderá ser acessada no endereço http://localhost:8000/docs

## Docker

Abaixo segue os comandos para execução com Docker

### Build

```bash
docker build -t 5mlet-app .
```

### Run

```bash
docker run -p 8000:8000 localhost/5mlet-app
```