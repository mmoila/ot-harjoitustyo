from database_connection import get_database_connection
from entities.budget import Budget


def get_budgets_by_rows(row):
    return Budget(row["name"], row["id"]) if row else None


class BudgetRepository:
    """Budjettien tietokannan hallinnasta vastaava luokka.

    Attributes: 
        conn = Tietokantaa kuvaava Connection-olio.
    """

    def __init__(self, connection):
        """Luokan konstruktori, joka alustaa yhteyden tietokantaan.

        Args:
            connection: Tietokantaa kuvaava Connection-olio.
        """

        self.conn = connection

    def create_budget(self, budget):
        """Luo tietokantaan uuden budjetin. 

        Args:
            budget: Budget-olio.
        """

        sql = "INSERT INTO budgets (name, user_id) values (:name, :user_id);"
        cursor = self.conn.cursor()
        cursor.execute(sql, {"name": budget.name, "user_id": budget.user_id})
        self.conn.commit()

    def delete_budget(self, budget):
        """Poistaa tietokannasta budjetin.

        Args:
            budget: Budget-olio.
        """

        sql = "DELETE FROM budgets WHERE id = :id"
        cursor = self.conn.cursor()
        cursor.execute(sql, {"id": budget.budget_id})
        self.conn.commit()

    def get_all_budgets(self, user_id):
        """Hakee tietokannasta kaikki tietyn käyttäjän budjetit.

        Args:
            user_id: Käyttäjän yksilöivä tunniste.

        Returns:
            Palauttaa listan käyttäjän budjeteista. Lista on tyhjä, jos yhtään 
            budjettia ei löydy.
        """

        sql = "SELECT id, name, user_id from budgets WHERE user_id=:user_id;"
        cursor = self.conn.cursor()
        cursor.execute(sql, {"user_id": user_id})
        rows = cursor.fetchall()
        budgets = list(map(get_budgets_by_rows, rows))
        for budget in budgets:
            budget.income = self.get_income(budget.budget_id)
            budget.expenses = self.get_expenses(budget.budget_id)
        return budgets

    def get_budget(self, id_):
        """Hakee tietokannasta budjetin tunnisteen mukaisen budjetin.

        Args:
            id_: Budjetin yksilöivä tunnus.

        Returns:
            Palauttaa Budget-olion. Jos tietokannasta ei löydy budjettia, 
            funktio palauttaa None.
        """

        sql = "SELECT id, name, user_id FROM budgets WHERE id=:id"
        cursor = self.conn.cursor()
        cursor.execute(sql, {"id": id_})
        row = cursor.fetchone()
        if row:
            budget = Budget(row["name"], row["id"], row["user_id"])
            budget.income = self.get_income(budget.budget_id)
            budget.expenses = self.get_expenses(budget.budget_id)
            return budget
        return None

    def get_income(self, budget_id):
        """Hakee tietokannasta budjettiin kuuluvat tulot.

        Args:
            budget_id: Budjetin yksilöivä tunnus.

        Returns:
            Palauttaa tupleista koostuvan listan. Jos tuloja ei ollut, funktio
            palauttaa tyhjän listan.
        """

        sql = "SELECT id, description, count from cash_flow\
            WHERE budget_id =:budget_id AND is_income = 1;"
        cursor = self.conn.cursor()
        cursor.execute(sql, {"budget_id": budget_id})
        data = cursor.fetchall()
        return [(d[0], d[1], d[2]) for d in data]

    def get_expenses(self, budget_id):
        """Hakee tietokannasta budjettiin kuuluvat tulot.

        Args:
            budget_id: Budjetin yksilöivä tunnus.

        Returns:
            Palauttaa tupleista koostuvan listan. Jos tuloja ei ollut, funktio
            palauttaa tyhjän listan.
        """

        sql = "SELECT id, description, count FROM cash_flow\
            WHERE budget_id =:budget_id AND is_income = 0;"
        cursor = self.conn.cursor()
        cursor.execute(sql, {"budget_id": budget_id})
        data = cursor.fetchall()
        return [(d[0], d[1], d[2]) for d in data]

    def add_income(self, description, count, budget_id):
        """Lisää tietokantaan budjetille uuden tulon.

        Args:
            description: Tulon kuvaus (esim. palkka).
            count: Tulon suuruus.
            budget_id: Budjetin yksilöivä tunnus.
        """

        sql = "INSERT INTO cash_flow (description, count, is_income, budget_id)\
            VALUES (:description, :count, 1, :budget_id);"
        cursor = self.conn.cursor()
        cursor.execute(sql, {"description": description,
                       "count": count, "budget_id": budget_id})
        self.conn.commit()

    def add_expense(self, description, count, budget_id):
        """Lisää tietokantaan budjetille uuden menon.

        Args:
            description: Menon kuvaus.
            count: Menon suuruus.
            budget_id: Budjetin yksilöivä tunnus.
        """

        sql = "INSERT INTO cash_flow (description, count, is_income, budget_id)\
            VALUES (:description, :count, 0, :budget_id);"
        cursor = self.conn.cursor()
        cursor.execute(sql, {"description": description,
                       "count": count, "budget_id": budget_id})
        self.conn.commit()

    def delete_cash_flow(self, id_, is_income):
        """Poistaa tietokannasta tunnisteen mukaisen tulon tai menon.

        Args:
            id_: Menon tai tulon yksilöivä tunnus.
            is_income: Totuusarvo kokonaislukuna 1 (True) tai 0 (False).
        """

        sql = "DELETE FROM cash_flow WHERE id=:id AND is_income =:is_income;"
        cursor = self.conn.cursor()
        cursor.execute(sql, {"id": id_, "is_income": is_income})
        self.conn.commit()

    def delete_all(self):
        """Poistaa tietokannasta kaikki budjetit ja niihin liittyvät tulot ja menot."""
        sql = "DELETE FROM budgets;\
               DELETE FROM cash_flow;"
        cursor = self.conn.cursor()
        cursor.executescript(sql)
        self.conn.commit()


budget_repository = BudgetRepository(get_database_connection())

if __name__ == "__main__":
    budget_repository.create("test", 1)
