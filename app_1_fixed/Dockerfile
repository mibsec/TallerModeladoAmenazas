FROM python:3.9-slim

# Crear usuario no-root
RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /app
COPY app.py .
RUN pip install --no-cache-dir flask

# Ejecutar como usuario no privilegiado
USER appuser

CMD ["python", "app.py"]
