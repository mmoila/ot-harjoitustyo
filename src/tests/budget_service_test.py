import unittest
from services.budget_service import BudgetService, UserNameExistsError


class FakeBudgetRepository():
    def __init__(self):
        self.budgets = []
        self.cash_flow_id = 0
        self.budget_id = 0

    def create_budget(self, budget):
        self.budget_id += 1
        budget.budget_id = self.budget_id
        budget.user_id = 1
        self.budgets.append(budget)

    def get_all_budgets(self, user_id):
        return [b for b in self.budgets if b.user_id == user_id]

    def get_budget(self, id_):
        for budget in self.budgets:
            if budget.budget_id == id_:
                return budget
        return None

    def delete_budget(self, budget):
        self.budgets.remove(budget)

    def get_income(self, budget_id):
        for budget in self.budgets:
            if budget.budget_id == budget_id:
                return budget.income
        return None

    def get_expenses(self, budget_id):
        for budget in self.budgets:
            if budget.budget_id == budget_id:
                return budget.expenses
        return None

    def add_income(self, description, count, budget_id):
        for budget in self.budgets:
            if budget.budget_id == budget_id:
                self.cash_flow_id += 1
                budget.income.append((self.cash_flow_id, description, count))

    def add_expense(self, description, count, budget_id):
        for budget in self.budgets:
            if budget.budget_id == budget_id:
                self.cash_flow_id += 1
                budget.expenses.append((self.cash_flow_id, description, count))

    def delete_cash_flow(self, id_, is_income=None):
        for budget in self.budgets:
            for i, income in enumerate(budget.income):
                if income[0] == id_:
                    budget.income.pop(i)
                    return
            for i, expense in enumerate(budget.expenses):
                if expense[0] == id_:
                    budget.expenses.pop(i)

    def delete_all(self):
        self.__init__()


class FakeUserRepository:
    def __init__(self):
        self.users = []
        self.user_id = 0

    def create_user(self, user):
        self.user_id += 1
        user.id = self.user_id
        self.users.append(user)

    def get_user(self, username, password):
        for user in self.users:
            if user.username == username:
                if user.password == password:
                    return user
        return None

    def check_user(self, username):
        for user in self.users:
            if user.username == username:
                return True
        return False

    def delete_all(self):
        self.__init__()


class TestBudgetService(unittest.TestCase):
    def setUp(self):
        self.budget_service = BudgetService(FakeBudgetRepository(),
                                            FakeUserRepository())
        self.budget1 = self.budget_service.create_budget("budget1", 1)
        self.budget2 = self.budget_service.create_budget("budget2", 1)

    def test_create_budget(self):
        self.budget_service.create_user("user1", "test1234")
        self.budget_service.login("user1", "test1234")

        self.assertEqual(self.budget1.name, "budget1")
        self.assertEqual(self.budget1.budget_id, 1)
        self.assertEqual(self.budget1.user_id, 1)

    def test_create_budget_with_invalid_name(self):
        budget = self.budget_service.create_budget("this_is_too_long_budget_name", 1)
        budget2 = self.budget_service.create_budget("", 1)

        self.assertFalse(budget)
        self.assertFalse(budget2)

    def test_delete_budget(self):
        self.budget_service.delete_budget(self.budget1)
        budget = self.budget_service.get_budget(1)
        self.assertIsNone(budget)

    def test_get_all_budgets(self):
        self.budget_service.create_user("user1", "test1234")
        self.budget_service.login("user1", "test1234")
        self.budget_service.create_budget("budget1")
        self.budget_service.create_budget("budget2")
        budgets = self.budget_service.get_all_budgets()

        self.assertEqual(budgets[0].budget_id, 1)
        self.assertEqual(budgets[0].name, "budget1")
        self.assertEqual(budgets[0].user_id, 1)
        self.assertEqual(budgets[1].budget_id, 2)
        self.assertEqual(budgets[1].name, "budget2")
        self.assertEqual(budgets[1].user_id, 1)

    def test_get_budget(self):
        budget = self.budget_service.get_budget(1)

        self.assertEqual(budget.name, "budget1")
        self.assertEqual(budget.budget_id, 1)
        self.assertEqual(budget.user_id, 1)

    def test_get_budget_income(self):
        self.budget_service.add_budget_income("income", 100, self.budget1)
        income = self.budget_service.get_budget_income(self.budget1)

        self.assertEqual(income[0][0], 1)
        self.assertEqual(income[0][1], "income")
        self.assertEqual(income[0][2], 100)

    def test_get_budget_expenses(self):
        self.budget_service.add_budget_expense("expense", 100, self.budget1)
        expense = self.budget_service.get_budget_expenses(self.budget1)

        self.assertEqual(expense[0][0], 1)
        self.assertEqual(expense[0][1], "expense")
        self.assertEqual(expense[0][2], 100)

    def test_add_invalid_income(self):
        self.budget_service.add_budget_income("", 100, self.budget1)
        income = self.budget_service.get_budget_income(self.budget1)
        self.budget_service.add_budget_income("income1", "number", self.budget1)
        self.assertEqual(len(income), 0)
        self.assertRaises(ValueError)

    def test_add_invalid_expense(self):
        self.budget_service.add_budget_expense("this_expense_is_too_long", 100, self.budget1)
        expense = self.budget_service.get_budget_expenses(self.budget1)
        self.budget_service.add_budget_expense("expense1", "number", self.budget1)
        self.assertEqual(len(expense), 0)
        self.assertRaises(ValueError)

    def test_delete_budget_income(self):
        self.budget_service.add_budget_income("income1", 100, self.budget1)
        self.budget_service.add_budget_income("income2", 200, self.budget1)
        self.budget_service.delete_budget_income(1)
        income = self.budget_service.get_budget_income(self.budget1)

        self.assertEqual(income[0][0], 2)
        self.assertEqual(income[0][1], "income2")
        self.assertEqual(income[0][2], 200)

    def test_delete_budget_expense(self):
        self.budget_service.add_budget_expense("expense1", 100, self.budget1)
        self.budget_service.add_budget_expense("expense2", 200, self.budget1)
        self.budget_service.delete_budget_expense(1)
        expense = self.budget_service.get_budget_expenses(self.budget1)

        self.assertEqual(expense[0][0], 2)
        self.assertEqual(expense[0][1], "expense2")
        self.assertEqual(expense[0][2], 200)

    def test_create_user(self):
        self.budget_service.create_user("user1", "test1234")
        user = self.budget_service.get_user("user1", "test1234")

        self.assertEqual(user.id, 1)
        self.assertEqual(user.username, "user1")
        self.assertEqual(user.password, "test1234")

    def test_create_user_that_already_exists(self):
        self.budget_service.create_user("user1", "test1234")
        with self.assertRaises(UserNameExistsError):
            self.budget_service.create_user("user1", "test98765")
        
        
    def test_login(self):
        self.budget_service.create_user("user1", "test1234")

        self.assertFalse(self.budget_service.login("user", "test1234"))
        self.assertTrue(self.budget_service.login("user1", "test1234"))
