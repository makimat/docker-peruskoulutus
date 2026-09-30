# Docker-peruskoulutus

Harjoitukset Dockerin peruskoulutukseen. Jokaisessa kansiossa on oma README, jossa on harjoituksen komennot ja selitykset.

## Ennen koulutusta

1. Asenna [Docker Desktop](https://www.docker.com/products/docker-desktop/) WSL2-taustalla ja käynnistä se.
2. Aseta Git käyttämään Linux-rivinvaihtoja:
   ```powershell
   git config --global core.autocrlf input
   ```
3. Kloonaa tämä repo:
   ```powershell
   git clone https://github.com/makimat/docker-peruskoulutus.git
   cd docker-peruskoulutus
   ```
4. Varmista, että Docker toimii:
   ```powershell
   docker run hello-world
   ```

## Harjoitukset

| Kansio | Aihe |
|---|---|
| [01-ensimmainen-kontti](01-ensimmainen-kontti/) | Kontti pystyyn, `docker ps`, `docker logs`, `docker exec` |
| [02-portti](02-portti/) | Kontin portti näkyviin hostille |
| [03-bind-mount](03-bind-mount/) | Hostin kansio kontin sisään |
| [04-dockerfile](04-dockerfile/) | Oma image Python-sovellukselle |
| [05-tekoalyagentit](05-tekoalyagentit/) | Dockerfile tekoälyagentilla ja tuloksen tarkistus |
| [06-volume](06-volume/) | Lisätehtävä: data, joka säilyy kontin poistamisen yli |

Komennot on kirjoitettu PowerShelliin. Bashissa korvaa `${PWD}` muodolla `$(pwd)`.

## Siivous

Harjoitusten jälkeen voit poistaa kaikki pysäytetyt kontit ja käyttämättömät imaget:

```powershell
docker system prune
```
