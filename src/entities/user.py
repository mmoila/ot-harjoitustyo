class User:
    """Luokka, joka kuvastaa yhtä käyttäjää.

    Attributes:
        id = Käyttäjän yksilöivä id.
        username = Käyttäjän käyttäjänimi.
        password = Käyttäjän salasana.
    """

    def __init__(self, username, password, id=None):
        """Luokan konstruktori, joka luo uuden käyttäjän. Konstruktori
        hyödyntää luokan asetusmetodeja käyttäjänimen ja salasanan validoinnissa.

        Args:
            username: Käyttäjän käyttäjänimi.
            password: Käyttäjän salasana.
            id: Käyttäjän yksilöivä tunniste. Saa oletuksena arvon None.
        """

        self.id = id
        self.username = username
        self.password = password

    @property
    def username(self):
        """Käyttäjän käyttäjätunnus.

        Returns:
            Palauttaa käyttäjän käyttäjätunnuksen.
        """

        return self.__username

    @property
    def password(self):
        """Käyttäjän salasana.

        Returns:
            Palauttaa käyttäjän salasanan.
        """

        return self.__password

    @username.setter
    def username(self, username):
        """Asettaa käyttäjälle käyttäjätunnuksen. Tarkistaa, että annettu
        salasana on oikean pituinen.

        Args:
            username: Käyttäjän käyttäjänimi.

        Raises:
            ValueError: Virhe, joka tapahtuu jos käyttäjätunnuksen pituus ei
            ole oikea.
        """

        if len(username) < 4 or len(username) > 20:
            raise ValueError("Username length must be between 4 and 20.")
        self.__username = username

    @password.setter
    def password(self, password):
        """Asettaa käyttäjälle salasanan. Tarkistaa, että annettu salasana 
        on oikean pituinen.

        Args:
            password: Käyttäjän salasana.

        Raises:
            ValueError: Virhe, joka tapahtuu jos salasanan pituus ei ole oikea
        """

        if len(password) < 8 or len(password) > 25:
            raise ValueError("Password length must be between 8 and 25.")
        self.__password = password
