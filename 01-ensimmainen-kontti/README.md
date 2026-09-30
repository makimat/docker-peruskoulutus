# 01 Ensimmäinen kontti

Käynnistetään nginx-verkkopalvelin kontissa ja katsotaan, mitä siellä tapahtuu.

## Käynnistä kontti

```powershell
docker run -d --name web nginx
```

- `-d` ajaa kontin taustalla
- `--name web` antaa kontille nimen, jolla siihen viitataan jatkossa
- `nginx` on image, josta kontti käynnistetään. Docker hakee sen Docker Hubista, jos sitä ei ole koneella.

## Katso käynnissä olevat kontit

```powershell
docker ps
```

Sarakkeessa `PORTS` lukee `80/tcp`. Nginx kuuntelee kontin sisällä porttia 80, mutta portti ei näy hostille. Selaimella palvelimeen ei siis vielä pääse. Se korjataan seuraavassa harjoituksessa.

## Lue kontin lokit

```powershell
docker logs web
```

Kontin lokit ovat prosessin stdout ja stderr. Lisää `-f`, niin lokit jäävät seuraamaan uusia rivejä. Lopeta painamalla Ctrl+C.

## Mene kontin sisään

```powershell
docker exec -it web bash
```

Kontin sisällä:

```bash
cat /etc/os-release   # Kontissa pyörii Debian, vaikka host on Windows
ls /usr/share/nginx/html
exit
```

## Siivoa

```powershell
docker rm -f web
```
