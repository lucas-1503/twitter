# Use uma imagem oficial do Python como imagem pai
FROM python:3.9-slim

# Defina variáveis de ambiente para Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Defina o diretório de trabalho no container
WORKDIR /code

# Instale dependências do sistema
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       postgresql-client \
       libpq-dev \
       gcc \
       npm \  
    && rm -rf /var/lib/apt/lists/*

# Instale dependências Python
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Instale o Bootstrap usando npm
RUN npm install bootstrap

# Copie os arquivos do projeto para o diretório de trabalho
COPY . .

# Exponha a porta 8000 para permitir comunicação com o servidor
EXPOSE 5432

# Comando para executar a aplicação
CMD ["python", "manage.py", "runserver", "0.0.0.0:5432"]
