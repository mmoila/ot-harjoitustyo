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
        return budget

    def get_all_budgets(self):
        budgets = self.__budget_repository.get_all_budgets()
        return budgets

    def get_budget(self, id_):
        budget = self.__budget_repository.get_budget(id_)
        return budget

    def get_budget_income(self, budget):
        return self.__budget_repository.get_income(budget.budget_id)

    def get_budget_expenses(self, budget):
        return self.__budget_repository.get_expenses(budget.budget_id)

    def add_budget_income(self, description, count, budget):
        self.__budget_repository.add_income(
            description, count, budget.budget_id)

    def add_budget_expense(self, description, count, budget):
        self.__budget_repository.add_expense(
            description, count, budget.budget_id)

    def delete_budget_income(self, id_, is_income=1):
        self.__budget_repository.delete_cash_flow(id_, is_income)

    def delete_budget_expense(self, id_, is_income=0):
        self.__budget_repository.delete_cash_flow(id_, is_income)


budget_service = BudgetService()
