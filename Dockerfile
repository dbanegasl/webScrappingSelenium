# Usa una imagen de Python
FROM python:3.9-slim

# Instala ChromeDriver
RUN apt-get update && \
    apt-get install -y \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos de tu proyecto al contenedor
COPY requirements.txt .
COPY app/ .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Ejecuta el script de web scraping al iniciar el contenedor
CMD ["python", "script.py"]
