import unittest
from services.budget_service import BudgetService
from entities.budget import Budget

class FakeBudgetRepository():
    def __init__(self):
        self.budgets = []
        self.cash_flow_id = 0
        self.budget_id = 0

    def create_budget(self, budget):
        self.budget_id += 1
        budget.budget_id = self.budget_id
        self.budgets.append(budget)

    def get_all_budgets(self):
        return self.budgets

    def get_budget(self, id_):
        for budget in self.budgets:
            if budget.budget_id == id_:
                return budget

    def get_income(self, budget_id):
        for budget in self.budgets:
            if budget.budget_id == budget_id:
                return budget.income

    def get_expenses(self, budget_id):
        for budget in self.budgets:
            if budget.budget_id == budget_id:
                return budget.expenses

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
    
    def delete_cash_flow(self, id_, is_income):
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



            
class TestBudgetService(unittest.TestCase):
    def setUp(self):
        self.budget_service = BudgetService(FakeBudgetRepository())
        
    def test_create_budget(self):
        budget = self.budget_service.create_budget("budget1")

        self.assertEqual(budget.name, "budget1")
        self.assertEqual(budget.budget_id, 1)

    def test_get_all_budgets(self):
        self.budget_service.create_budget("budget1")
        self.budget_service.create_budget("budget2")
        budgets = self.budget_service.get_all_budgets()

        self.assertEqual(budgets[0].budget_id, 1)
        self.assertEqual(budgets[0].name, "budget1")
        self.assertEqual(budgets[1].budget_id, 2)
        self.assertEqual(budgets[1].name, "budget2")

    def test_get_budget(self):
        self.budget_service.create_budget("budget1")
        budget = self.budget_service.get_budget(1)

        self.assertEqual(budget.name, "budget1")
        self.assertEqual(budget.budget_id, 1)

    def test_get_budget_income(self):
        budget = self.budget_service.create_budget("budget1")
        self.budget_service.add_budget_income("income", 100, budget)
        income = self.budget_service.get_budget_income(budget)

        self.assertEqual(income[0][0], 1)
        self.assertEqual(income[0][1], "income")
        self.assertEqual(income[0][2], 100)

    def test_get_budget_expenses(self):
        budget = self.budget_service.create_budget("budget1")
        self.budget_service.add_budget_expense("expense", 100, budget)
        expense = self.budget_service.get_budget_expenses(budget)

        self.assertEqual(expense[0][0], 1)
        self.assertEqual(expense[0][1], "expense")
        self.assertEqual(expense[0][2], 100)

    def test_delete_budget_income(self):
        budget = self.budget_service.create_budget("budget1")
        self.budget_service.add_budget_income("income1", 100, budget)
        self.budget_service.add_budget_income("income2", 200, budget)
        self.budget_service.delete_budget_income(1)
        income = self.budget_service.get_budget_income(budget)

        self.assertEqual(income[0][0], 2)
        self.assertEqual(income[0][1], "income2")
        self.assertEqual(income[0][2], 200)


    def test_delete_budget_expense(self):
        budget = self.budget_service.create_budget("budget1")
        self.budget_service.add_budget_expense("expense1", 100, budget)
        self.budget_service.add_budget_expense("expense2", 200, budget)
        self.budget_service.delete_budget_expense(1)
        expense = self.budget_service.get_budget_expenses(budget)

        self.assertEqual(expense[0][0], 2)
        self.assertEqual(expense[0][1], "expense2")
        self.assertEqual(expense[0][2], 200)
        
    

        

        
        
