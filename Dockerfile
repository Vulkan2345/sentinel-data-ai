FROM python:3.11-slim

# Evitar que python escriba archivos .pyc y no buffer salida
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Crear un usuario no root por seguridad
RUN addgroup --system appgroup && adduser --system --group appuser

WORKDIR /app

# Instalar libmagic (necesario para python-magic)
RUN apt-get update && apt-get install -y --no-install-recommends libmagic1 && \
    rm -rf /var/lib/apt/lists/*

# Copiar requirements e instalar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY ./app /app/app

# Cambiar permisos y cambiar al usuario no root
RUN chown -R appuser:appgroup /app
USER appuser

EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
