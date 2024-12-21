# Usar uma imagem base do Python
FROM python:3.11-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar o arquivo requirements.txt (que contém todas as dependências)
COPY requirements.txt /app/

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código do projeto para dentro do container
COPY . /app/

# Expor a porta que o Django vai rodar (por padrão, 8000)
EXPOSE 8000

# Rodar o servidor do Django ao iniciar o container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
