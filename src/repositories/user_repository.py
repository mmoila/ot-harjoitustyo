from werkzeug.security import generate_password_hash, check_password_hash
from database_connection import get_database_connection
from entities.user import User


class UserRepository:
    """Käyttäjätietojen tietokannasta vastaava luokka.

    Attributes:
        conn = Tietokantaa kuvaava Connection-olio.
    """

    def __init__(self, connection):
        """Luokan konstruktori, joka alustaa yhteyden tietokantaan.

        Args:
            connection: Tietokantaa kuvaava Connection-olio.
        """

        self.conn = connection

    def create_user(self, user):
        """Luo tietokantaan uuden käyttäjän.

        Args:
            user: User-olio.
        """

        hash_value = generate_password_hash(user.password)
        sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
        cursor = self.conn.cursor()
        cursor.execute(
            sql, {"username": user.username, "password": hash_value})
        self.conn.commit()

    def get_user(self, username, password):
        """Hakee tietokannasta käyttäjän, jos käyttäjätunnus ja salasana täsmäävät.

        Args:
            username: Käyttäjän käyttäjätunnus.
            password: Käyttäjän salasana.

        Returns:
            Jos käyttäjä löytyy tietokannasta, palauttaa User-olion. 
        """

        sql = "SELECT id, username, password FROM users WHERE username=:username"
        cursor = self.conn.cursor()
        cursor.execute(sql, {"username": username})
        row = cursor.fetchone()
        if row and check_password_hash(row["password"], password):
            return User(row["username"], password, row["id"])

    def check_user(self, username):
        """Tarkastaa löytyykö tietokannasta annetulla käyttäjänimella käyttäjää.

        Args:
            username: Käyttäjän käyttäjänimi.

        Returns:
            Jos käyttäjä löytyy tietokannasta, palauttaa True. Muuten palautta False.
        """

        sql = "SELECT 1 FROM users WHERE username=:username"
        cursor = self.conn.cursor()
        cursor.execute(sql, {"username": username})
        row = cursor.fetchone()
        if row:
            return True
        return False

    def delete_all(self):
        """Poistaa kaikki käyttäjät tietokannasta.
        """

        sql = "DELETE FROM users"
        cursor = self.conn.cursor()
        cursor.execute(sql)
        self.conn.commit()


user_repository = UserRepository(get_database_connection())
