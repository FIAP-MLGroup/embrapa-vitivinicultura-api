# Trabalho Pós-Graduação - FIAP 5MLET

Extração dos dados de vitivinicultura fornecidos no site da EMBRAPA.

## Visão macro dos componentes

![Visão Macro](assets/images/overview.png)

## 🔧 Bootstrap (modo tradicional)

Para inicialização deste projeto manualmente, execute os comandos abaixo:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## ▶️ Startup (modo tradicional)

Para iniciar o servidor web localmente:

```bash
uvicorn app.main:app --no-server-header --reload
```

A API estará disponível no endereço: [http://localhost:8000/](http://localhost:8000/)

A documentação interativa OpenAPI (Swagger) pode ser acessada em:  
[http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🐍 Alternativa com Makefile

Se preferir automatizar os passos acima com `make`:

```bash
make init      # Cria o ambiente virtual e instala dependências
```

> ⚠️ Após executar `make init`, você ainda precisa ativar o ambiente com:

```bash
source .venv/bin/activate
```

E então iniciar com:

```bash
make dev       # Roda localmente com uvicorn
```

---

## 🐳 Docker

### Build e execução tradicionais:

```bash
docker build -t 5mlet-app .
docker run -p 8000:8000 5mlet-app
```

### Ou com Makefile:

```bash
make docker
```

> Esse comando **builda automaticamente** a imagem (`make build-docker`) e já executa localmente com `docker run`.

Se quiser apenas construir a imagem (sem rodar), use:

```bash
make build-docker
```

---

## 🧪 Lambda Local (SAM CLI)

Para simular a execução como função Lambda localmente com SAM:

```bash
make lambda
```

> Esse comando também **builda a imagem Lambda automaticamente** (`make build-lambda`) antes de executar via SAM CLI.

A API estará acessível em:  
[http://localhost:3000/docs](http://localhost:3000/docs)

> ⚠️ Isso **não envia a aplicação para a AWS** — é apenas uma simulação local.

Se quiser apenas construir a imagem (sem rodar), use:

```bash
make build-lambda
```

> Para implantar na AWS, publique a imagem em um repositório ECR.

---

## 🔐 JWT

### Obter token JWT:

```bash
curl -X POST http://localhost:8000/api/v1/auth \
  -H "Content-Type: application/x-www-form-urlencoded" \
  --data "username=admin" \
  --data "password=admin"
```

### Chamada autenticada:

```bash
curl http://localhost:8000/api/v1/producao \
  -H "Authorization: Bearer <SEU_TOKEN_JWT>"
```

Também é possível autenticar pelo botão "Authorize" no Swagger UI:

![Swagger Authorize](assets/images/authorize.png)

---

## ✅ Pré-requisitos

- Python 3.11+
- Docker (para build/run local e Lambda)
- AWS SAM CLI (para testes locais simulando Lambda)
