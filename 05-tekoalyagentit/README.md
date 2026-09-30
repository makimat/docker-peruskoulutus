# 05 Tekoälyagentit

Agentti kirjoittaa Dockerfilen nopeasti, mutta tulos pitää aina tarkistaa. Mitä tarkemmin kerrot vaatimukset, sitä vähemmän agentti arvaa.

## Esimerkkiprompti

> Kirjoita tuotantovalmis Dockerfile Python FastAPI -sovellukselle. Käytä kevyttä python-slim-base-imagea. Optimoi kerrosten välimuistitus (layer caching) erottamalla requirements.txt-asennus omaksi vaiheekseen. Aja sovellus non-root-käyttäjällä. Lisää mukaan myös .dockerignore-tiedosto.

Kokeile promptia tyhjässä kansiossa, jossa on vain `04-dockerfile`-kansion `main.py` ja `requirements.txt`. Vertaa tulosta valmiiseen Dockerfileen.

## Tarkistuslista

1. **Ei root-käyttäjää.** Dockerfilessä on `USER`-rivi. Kubernetes-klusterit voivat estää root-kontit.
2. **.dockerignore on olemassa.** Siinä on ainakin `.git`, `.venv`, `__pycache__`, `*.pyc` ja `.env`. Muuten salaisuudet ja turhat tiedostot päätyvät imageen.
3. **Lokit stdoutiin.** Sovellus ei kirjoita lokeja tiedostoon kontin sisällä. Muuten `docker logs` ja Kubernetes eivät näe niitä.
4. **Rivinvaihdot LF.** Windowsilla tallennettu skripti CRLF-rivinvaihdoilla kaatuu kontissa virheeseen `/bin/sh^M: bad interpreter`. Tarkista rivinvaihdot editorin alapalkista.
5. **Base image on pieni ja versioitu.** Esimerkiksi `python:3.11-slim`, ei `python:latest`.
