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
    def __init__(self, budget_repository=default_budget_repository,
                 user_repository=default_user_repository):
        self.__budget_repository = budget_repository
        self.user_repository = user_repository
        self.user = None

    def create_budget(self, name, user_id=None):
        if not user_id:
            user_id = self.user.id
        budget = Budget(name, user_id=user_id)
        self.__budget_repository.create_budget(budget)
        return budget

    def get_all_budgets(self, user_id=None):
        if not user_id:
            user_id = self.user.id
        budgets = self.__budget_repository.get_all_budgets(user_id)
        return budgets

    def get_budget(self, id_):
        budget = self.__budget_repository.get_budget(id_)
        return budget

    def get_budget_income(self, budget):
        return self.__budget_repository.get_income(budget.budget_id)

    def get_budget_expenses(self, budget):
        return self.__budget_repository.get_expenses(budget.budget_id)

    def add_budget_income(self, description, count, budget):
        if float(count):
            count = float(count)
            self.__budget_repository.add_income(
                description, count, budget.budget_id)

    def add_budget_expense(self, description, count, budget):
        if float(count):
            count = float(count) 
            self.__budget_repository.add_expense(
                description, count, budget.budget_id)

    def delete_budget_income(self, id_, is_income=1):
        self.__budget_repository.delete_cash_flow(id_, is_income)

    def delete_budget_expense(self, id_, is_income=0):
        self.__budget_repository.delete_cash_flow(id_, is_income)

    def delete_budget(self, budget):
        self.__budget_repository.delete_budget(budget)

    def create_user(self, username, password):
        if self.user_repository.check_user(username):
            raise UserNameExistsError("Username already exists!")
        user = User(username=username, password=password)
        self.user_repository.create_user(user)

    def get_user(self, username, password):
        return self.user_repository.get_user(username, password)

    def login(self, username, password):
        self.user = self.get_user(username, password)
        if self.user:
            return True
        return False


budget_service = BudgetService()
