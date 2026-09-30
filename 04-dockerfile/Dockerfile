# 1. Pieni base image
FROM python:3.11-slim

# 2. Työskentelyhakemisto
WORKDIR /app

# 3. Riippuvuudet ensin, jotta pip-asennus jää välimuistiin (layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Muu sovelluskoodi
COPY . .

# 5. Ei ajeta root-käyttäjänä
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# 6. Portti ja käynnistyskomento
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
