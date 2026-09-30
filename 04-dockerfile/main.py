import logging

from fastapi import FastAPI

# Lokit stdoutiin, jotta docker logs ja Kubernetes näkevät ne
logging.basicConfig(level=logging.INFO)
log = logging.getLogger("oma-api")

app = FastAPI()


@app.get("/")
def root():
    log.info("Etusivua pyydettiin")
    return {"viesti": "Hei kontin sisältä!"}


@app.get("/health")
def health():
    return {"status": "ok"}
