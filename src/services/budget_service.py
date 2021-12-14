from repositories.budget_repository import (
    budget_repository as default_budget_repository
)

from repositories.user_repository import (
    user_repository as default_user_repository
)

from entities.budget import Budget
from entities.user import User


class UserNameExistsError(Exception):
    pass


class BudgetService:
    """Ohjelman sovelluslogiikasta vastaava luokka."""
    def __init__(self, budget_repository=default_budget_repository,
                 user_repository=default_user_repository):
        """Luokan konstruktori.

        Args:
            budget_repository: Budjettien tietokantaoperaatioita hallinnoivan luokan ilmentymä.
            Oletusarvona BudgetRepository-olio.
            user_repository: Käyttäjien tietokantaoperaatioita hallinnoivan luokan ilmentymä.
            Oletuksena UserRepository-olio.
            user: User-olio.
        """

        self.__budget_repository = budget_repository
        self.__user_repository = user_repository
        self.__user = None

    def create_budget(self, name, user_id=None):
        """Luo uuden budjetin.

        Args:
            name: Budjetin nimi.
            user_id: Käyttäjän yksilöivä tunniste. Saa oletuksena arvon None.

        Returns:
            Palauttaa Budget-olion.
        """

        if not user_id:
            user_id = self.__user.id
        budget = Budget(name, user_id=user_id)
        self.__budget_repository.create_budget(budget)
        return budget

    def get_all_budgets(self, user_id=None):
        """Palauttaa käyttäjän kaikki budjetit.

        Args:
            user_id: Käyttäjän yksilöivä tunniste. Saa oletuksena arvon None.

        Returns:
            Palauttaa Budget-olioista koostuvan listan.
        """

        if not user_id:
            user_id = self.__user.id
        budgets = self.__budget_repository.get_all_budgets(user_id)
        return budgets

    def get_budget(self, id_):
        """Palauttaa tunnisteen mukaisen budjetin.

        Args:
            id_: Budjetin yksilöivä tunniste.

        Returns:
            Palauttaa Budget-olion. 
        """

        budget = self.__budget_repository.get_budget(id_)
        return budget

    def get_budget_income(self, budget):
        """Palauttaa budjetin tulot.

        Args:
            budget: Budget-olio.

        Returns:
            Palauttaa tupleista koostuvan listan. Jos tuloja ei ollut, funktio
            palauttaa tyhjän listan. Tuplet ovat muotoa (id, description, count).
        """

        return self.__budget_repository.get_income(budget.budget_id)

    def get_budget_expenses(self, budget):
        """Palauttaa budjetin menot.

        Args:
            budget: Budget-olio.

        Returns:
            Palauttaa tupleista koostuvan listan. Jos tuloja ei ollut, funktio
            palauttaa tyhjän listan. Tuplet ovat muotoa (id, description, count).
        """

        return self.__budget_repository.get_expenses(budget.budget_id)

    def add_budget_income(self, description, count, budget):
        """Lisää budjettiin tulon.

        Args:
            description: Kuvaus tulosta.
            count: Tulon määrä.
            budget: Budget-olio.
        """

        try:
            count = float(count)
            self.__budget_repository.add_income(
                description, count, budget.budget_id)
        except ValueError:
            pass

    def add_budget_expense(self, description, count, budget):
        """Lisää budjettiin menon.

        Args:
            description: Kuvaus menosta.
            count: Menon määrä.
            budget: Budget-olio.
        """

        try:
            count = float(count) 
            self.__budget_repository.add_expense(
                description, count, budget.budget_id)
        except ValueError:
            pass

    def delete_budget_income(self, id_, is_income=1):
        """Poistaa budjetista yhden tulon.

        Args:
            id_: Tulon yksilöivä id.
            is_income: Totuusarvo kokonaislukuna 1 (True) tai 0 (False). 
            Oletuksena arvo 1.
        """

        self.__budget_repository.delete_cash_flow(id_, is_income)

    def delete_budget_expense(self, id_, is_income=0):
        """Poistaa budjetista yhden menon.

        Args:
            id_: Menon yksilöivä id.
            is_income: Totuusarvo kokonaislukuna 1 (True) tai 0 (False). 
            Oletuksena arvo 0.
        """

        self.__budget_repository.delete_cash_flow(id_, is_income)

    def delete_budget(self, budget):
        """Poistaa budjetin.

        Args:
            budget: Budget-olio.
        """

        self.__budget_repository.delete_budget(budget)

    def create_user(self, username, password):
        """Luo uuden käyttäjän.

        Args:
            username: Käyttäjätunnus.
            password: Salasana.

        Raises:
            UserNameExistsError, jos käyttäjänimi on jo olemassa.
        """

        if self.__user_repository.check_user(username):
            raise UserNameExistsError("Username already exists!")
        user = User(username=username, password=password)
        self.__user_repository.create_user(user)

    def get_user(self, username, password):
        """Hakee argumenttien mukaisen käyttäjän. 

        Args:
            username: Käyttäjänimi.
            password: Salasana.

        Returns:
            Palauttaa Budget-olion, jos käyttäjä ja salasana täsmäävät tietokantaan
            tallennettuihin tietoihin. Muulloin palauttaa None.
        """

        return self.__user_repository.get_user(username, password)

    def login(self, username, password):
        """Käsittelee käyttäjän sisäänkirjautumisen.

        Args:
            username: Käyttäjänimi.
            password: Salasana.

        Returns:
            Palauttaa User-olion jos käyttäjänimi ja salasana täsmäävät. Muuten
            palauttaa False.
        """

        self.__user = self.get_user(username, password)
        if self.__user:
            return self.__user
        return False


budget_service = BudgetService()
