import unittest
from repositories.budget_repository import budget_repository
from entities.budget import Budget


class TestBudgetRepository(unittest.TestCase):
    def setUp(self):
        budget_repository.delete_all()
        self.budget1 = Budget("budget1")
        self.budget2 = Budget("budget2")

    def test_create_budget(self):
        budget_repository.create_budget(self.budget1)
        budgets = budget_repository.get_all_budgets()

        self.assertEqual(budgets[0].name, "budget1")

    def test_get_all_budgets(self):
        budget_repository.create_budget(self.budget1)
        budget_repository.create_budget(self.budget2)
        budgets = budget_repository.get_all_budgets()

        self.assertEqual(len(budgets), 2)
        self.assertEqual(budgets[0].budget_id, 1)
        self.assertEqual(budgets[1].budget_id, 2)

    def test_get_budget(self):
        budget_repository.create_budget(self.budget1)
        budget = budget_repository.get_budget(1)

        self.assertEqual(budget.budget_id, 1)
        self.assertEqual(budget.name, "budget1")
        self.assertEqual(budget.user_id, None)

    def test_add_income(self):
        budget_repository.create_budget(self.budget1)
        budget_repository.add_income("income", 100, 1)
        income = budget_repository.get_income(1)

        self.assertEqual(income[0][0], 1)
        self.assertEqual(income[0][1], "income")
        self.assertEqual(income[0][2], 100)

    def test_add_expense(self):
        budget_repository.create_budget(self.budget1)
        budget_repository.add_expense("expense", 100, 1)
        expense = budget_repository.get_expenses(1)

        self.assertEqual(expense[0][0], 1)
        self.assertEqual(expense[0][1], "expense")
        self.assertEqual(expense[0][2], 100)

    def test_delete_cash_flow(self):
        budget_repository.create_budget(self.budget1)
        budget_repository.add_expense("expense1", 100, 1)
        budget_repository.add_expense("expense2", 200, 1)
        budget_repository.delete_cash_flow(1, 0)
        expenses = budget_repository.get_expenses(1)

        self.assertEqual(expenses[0][0], 2)
        self.assertEqual(expenses[0][1], "expense2")
        self.assertEqual(expenses[0][2], 200)

        

    
