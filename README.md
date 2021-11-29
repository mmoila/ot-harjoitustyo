# Budjetointisovellus (Ohjelmistotekniikka harjoitustyö)

Sovelluksen avulla käyttäjät voivat luoda budjetteja, joissa voi vertailla tulojen ja menojen suhdetta.
Yhdellä käyttäjällä voi olla useampia itse nimeämiään budjetteja.

## Dokumentaatio

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

