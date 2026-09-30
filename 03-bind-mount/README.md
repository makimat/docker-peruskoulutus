# 03 Bind mount

Bind mount näyttää hostin kansion kontin sisällä. Kansio ei kopioidu konttiin, vaan kontti lukee samoja tiedostoja kuin sinun editorisi.

## Käynnistä kontti

Mene tähän kansioon ja käynnistä nginx niin, että kansio `sivusto` näkyy nginxin sisältökansiona:

```powershell
cd 03-bind-mount
docker run -d --name sivusto -p 8080:80 -v ${PWD}/sivusto:/usr/share/nginx/html nginx
```

`-v` toimii kuten `-p`: vasemmalla hostin polku, oikealla polku kontin sisällä.

Avaa selaimessa http://localhost:8080 ja klikkaile sivujen välillä.

## Muokkaa sivua

1. Avaa `sivusto/index.html` editorissa.
2. Muuta otsikkoa ja tallenna.
3. Päivitä selain.

Muutos näkyy heti ilman kontin uudelleenkäynnistystä.

## Katso kontin sisältä

```powershell
docker exec sivusto ls -la /usr/share/nginx/html
```

Samat tiedostot kuin hostin `sivusto`-kansiossa. Luo hostilla uusi tiedosto ja aja komento uudelleen.

## Siivoa

```powershell
docker rm -f sivusto
```

Tiedostot jäävät hostille, koska ne olivat siellä koko ajan.
