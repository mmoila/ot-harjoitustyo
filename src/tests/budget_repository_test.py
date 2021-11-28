import unittest
from repositories.budget_repository import budget_repository
from entities.budget import Budget


class TestBudgetRepository(unittest.TestCase):
    def setUp(self):
        self.budget1 = Budget("budget1")

    def test_create_budget(self):
        budget_repository.create_budget(self.budget1)
        budgets = budget_repository.get_all_budgets()

        self.assertEqual(budgets[0].name, "budget1")
