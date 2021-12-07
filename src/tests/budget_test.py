import unittest
from entities.budget import Budget


class TestBudget(unittest.TestCase):
    def setUp(self):
        self.budget = Budget("test_budget", 1, 1)
        self.budget.income = [(1, "income1", 100), (2, "income2", 200)]
        self.budget.expenses = [(3, "expense1", 120), (4, "expense2", 150)]

    def test_get_balance(self):
        balance = self.budget.get_balance()
        self.assertEqual(balance, 30)
