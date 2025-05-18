# Imagem base oficial do Python
FROM python:3.13-alpine

# Diretório de trabalho dentro do contêiner
WORKDIR /app

# Instala os pacotes de build necessários para compilar dependências
RUN apk add --no-cache \
    build-base \
    gcc \
    musl-dev \
    python3-dev \
    libffi-dev

# Copia o arquivo de dependências
COPY requirements.txt .

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código do projeto
COPY app ./app

# Ajuste de permissões para compatibilidade com UID arbitrário
RUN chgrp -R 0 /app && \
    chmod -R g=u /app

# Define o usuário arbitrário
USER 1001

# Expõe a porta onde o FastAPI será executado
EXPOSE 8000

# Comando para iniciar o servidor FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--no-server-header"]