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

## JWT

Exemplo de chamada para obter token JWT:
```bash
curl -X POST http://localhost:8000/api/v1/auth \        
  -H "Content-Type: application/x-www-form-urlencoded" \                                                                                                
  --data "username=admin&password=admin"
```

Exemplo de chamada para endpoint autenticado:
```bash
curl http://localhost:8000/api/v1/producao_autenticado \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTc0NTk1NzI2Mn0.C4W8ApBMQCNpSdpJqul06vFr11JvYQ23drdPF6dRBLc"
```

ou

Informar o token ao clicar em Authorize no SwaggerUI:

![Swagger Authorize](assets/images/authorize.png)