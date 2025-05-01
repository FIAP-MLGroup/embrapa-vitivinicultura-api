APP_NAME=vitivinicultura
LAMBDA_IMAGE=$(APP_NAME):lambda
DOCKER_IMAGE=$(APP_NAME):local

.PHONY: init dev docker lambda build-docker build-lambda

init:
	@echo "🐍 Criando ambiente virtual..."
	python3 -m venv .venv
	@echo "📦 Instalando dependências..."
	. .venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt
	@echo "✅ Ambiente virtual pronto! Use: source .venv/bin/activate"

dev:
	@echo "▶️ Iniciando FastAPI localmente com Uvicorn..."
	. .venv/bin/activate && uvicorn app.main:app --reload

docker: build-docker
	docker run -p 8000:8000 $(DOCKER_IMAGE)

lambda: build-lambda
	sam local start-api

build-docker:
	docker build -t $(DOCKER_IMAGE) -f Dockerfile .

build-lambda:
	docker build --platform linux/amd64 -t $(LAMBDA_IMAGE) -f DockerfileLambda .
