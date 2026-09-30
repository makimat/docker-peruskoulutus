# 06 Volume (lisätehtävä)

Kontin omat muutokset katoavat, kun kontti poistetaan. Volume on Dockerin hallinnoima tallennustila, joka säilyy konttien välillä. Tyypillinen käyttö on tietokannan data.

## Ilman volumea muutokset katoavat

Käynnistä nginx ja muuta etusivua kontin sisällä:

```powershell
docker run -d --name web -p 8080:80 nginx
docker exec web sh -c "echo '<h1>Muokattu</h1>' > /usr/share/nginx/html/index.html"
```

Avaa http://localhost:8080. Sivulla lukee "Muokattu".

Poista kontti ja luo se uudelleen:

```powershell
docker rm -f web
docker run -d --name web -p 8080:80 nginx
```

Päivitä selain. Nginxin oletussivu on palannut, koska uusi kontti alkaa aina imagen puhtaalta pöydältä.

```powershell
docker rm -f web
```

## Volumen kanssa muutokset säilyvät

Tee sama uudelleen, mutta nyt html-kansio on volume nimeltä `html`:

```powershell
docker run -d --name web -p 8080:80 -v html:/usr/share/nginx/html nginx
docker exec web sh -c "echo '<h1>Muokattu</h1>' > /usr/share/nginx/html/index.html"
```

Docker luo volumen automaattisesti ja kopioi siihen imagen alkuperäiset tiedostot. Tarkista selaimesta, että sivulla lukee "Muokattu".

Poista kontti ja luo se uudelleen samalla volumella:

```powershell
docker rm -f web
docker run -d --name web -p 8080:80 -v html:/usr/share/nginx/html nginx
```

Päivitä selain. Muutos on tallessa, koska se oli volumessa eikä kontissa.

## Bind mount vai volume?

| | Bind mount | Volume |
|---|---|---|
| Missä data on | Hostin kansiossa, jonka itse valitset | Dockerin hallinnoimassa paikassa |
| Syntaksi | `-v ${PWD}/kansio:/polku` | `-v nimi:/polku` |
| Tyypillinen käyttö | Lähdekoodi kehityksen aikana | Tietokannan data |

## Siivoa

```powershell
docker rm -f web
docker volume ls
docker volume rm html
```
