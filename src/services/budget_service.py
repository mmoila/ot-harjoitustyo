from repositories.budget_repository import (
    budget_repository as default_budget_repository
)

from entities.budget import Budget


class BudgetService:
    def __init__(self, budget_repository=default_budget_repository):
        self.__budget_repository = budget_repository

    def create_budget(self, name, user_id=None):
        budget = Budget(name, user_id)
        self.__budget_repository.create_budget(budget)

    def get_all_budgets(self):
        budgets = self.__budget_repository.get_all_budgets()
        return budgets

    def get_budget_income(self, budget_id):
        return self.__budget_repository.get_income(budget_id)

    def get_budget_expenses(self, budget_id):
        return self.__budget_repository.get_expenses(budget_id)

    def add_budget_income(self, count, budget_id):
        self.__budget_repository.add_income(count, budget_id)

    def add_budget_expense(self, count, budget_id):
        self.__budget_repository.add_expense(count, budget_id)


budget_service = BudgetService()