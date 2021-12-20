# Budjetointisovellus (Ohjelmistotekniikka harjoitustyö)

Sovelluksen avulla käyttäjät voivat luoda budjetteja, joissa voi vertailla tulojen ja menojen suhdetta.
Yhdellä käyttäjällä voi olla useampia itse nimeämiään budjetteja.

## Dokumentaatio
[Sovelluksen viimeisimmän version release](https://github.com/mmoila/ot-harjoitustyo/releases/tag/viikko6)<br>
[Käyttöohje](https://github.com/mmoila/ot-harjoitustyo/tree/master/dokumentaatio/kayttoohje.md)<br>
[Vaatimusmäärittely](https://github.com/mmoila/ot-harjoitustyo/tree/master/dokumentaatio/vaatimusmaarittely.md)<br>
[Tuntikirjanpito](https://github.com/mmoila/ot-harjoitustyo/tree/master/dokumentaatio/tuntikirjanpito.md)<br>
[Arkkitehtuurikuvaus](https://github.com/mmoila/ot-harjoitustyo/tree/master/dokumentaatio/arkkitehtuuri.md)

## Asennus

Sovellus tarvitsee toimiakseen vähintään Python 3.8 version sekä kirjastojen ja riippuvuuksien hallintaa varten Poetryn.<br>
Poetryn pystyy asentamaan esimerkiksi linuxissa komennolla<br>
```bash
    pip3 install poetry
```

1. Asenna riippuvuudet komennolla<br>
```bash
    poetry install
```

2. Alusta tietokanta komennolla<br>
```bash
    poetry run invoke build
```

3. Käynnistä sovellus komennolla<br>
```bash
    poetry run invoke start
```

## Muut komentorivillä suoritettavat toiminnot

### Testien ajaminen

```bash
    poetry run invoke test
```

### Testikattavuusraportin luominen
Komento luo projektin juurikansioon kansion htmlcov, joka sisältää index.html-tiedoston. 
Tämän tiedoston avaamalla saa auki testikattavuusraportin

```bash
    poetry run invoke coverage-report
```

### Pylint tarkistuksen ajaminen
Komento luo projektin juurihakemistossa olevan .pylintrc-tiedoston mukaisen koodin laaduntarkistuksen.

```bash
    poetry run invoke lint
```

### Autopep korjauksen ajaminen
Komento ajaa koodille automaattisen korjauksen autopep8-kirjaston avulla.

```bash
    poetry run invoke autopep
```

