# 02 Portti hostille

Kontti on eristetty hostista myös verkon osalta. Portti avataan hostille erikseen.

## Käynnistä kontti portin kanssa

```powershell
docker run -d --name web -p 8080:80 nginx
```

`-p 8080:80` tarkoittaa: hostin portti 8080 ohjataan kontin porttiin 80. Vasemmalla on aina host, oikealla kontti.

Avaa selaimessa http://localhost:8080

## Seuraa lokeja

```powershell
docker logs -f web
```

Päivitä selainta muutaman kerran. Jokainen pyyntö näkyy lokissa omana rivinään. Lopeta seuraaminen painamalla Ctrl+C.

## Kokeile

- Mitä `docker ps` näyttää nyt `PORTS`-sarakkeessa?
- Käynnistä toinen kontti hostin porttiin 8081. Mitä tapahtuu, jos yrität käyttää samaa hostin porttia 8080 kahdesti?

## Siivoa

```powershell
docker rm -f web
```
