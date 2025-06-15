FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    dos2unix \
    libpq-dev \
    gcc \
    default-libmysqlclient-dev \
    default-mysql-client \         
    pkg-config \
    build-essential \
    && apt-get clean

# Instala dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
