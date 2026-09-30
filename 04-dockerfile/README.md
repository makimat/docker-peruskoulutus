# 04 Dockerfile

Rakennetaan oma image pienelle FastAPI-sovellukselle. Kansiossa on valmiina `main.py`, `requirements.txt`, `Dockerfile` ja `.dockerignore`.

## Rakenna ja käynnistä

```powershell
cd 04-dockerfile
docker build -t oma-api .
docker run -d --name api -p 8000:8000 oma-api
```

Avaa http://localhost:8000 ja http://localhost:8000/docs

## Tarkista

```powershell
docker logs api           # Sovelluksen lokit tulevat stdoutiin
docker exec api whoami    # appuser, ei root
docker exec api ls -la    # .dockerignoren tiedostot puuttuvat
```

## Layer caching

1. Muuta `main.py`:ssä viestiä ja rakenna uudelleen: `docker build -t oma-api .`
   Riippuvuuksien asennus näyttää `CACHED`, koska `requirements.txt` ei muuttunut.
2. Lisää `requirements.txt`:hen rivi `httpx` ja rakenna uudelleen.
   Nyt pip-asennus ajetaan uudestaan.

Siksi `requirements.txt` kopioidaan ennen muuta koodia: koodi muuttuu usein, riippuvuudet harvoin.

## Siivoa

```powershell
docker rm -f api
```
