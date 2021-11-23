from database_connection import get_database_connection
from entities.budget import Budget

def get_budgets_by_rows(row):
    return Budget(row["name"], row["id"]) if row else None

class BudgetRepository:
    def __init__(self, connection): 
        self.conn = connection

    def create_budget(self, budget):
        sql = "INSERT INTO budgets (name, user_id) values (:name, :user_id);"
        cursor = self.conn.cursor()
        cursor.execute(sql, {"name": budget.name, "user_id": budget.user_id})
        self.conn.commit()

    def get_all_budgets(self):
        sql = "SELECT id, name, user_id from budgets;"
        cursor = self.conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        budgets = list(map(get_budgets_by_rows, rows))
        for budget in budgets:
            budget.income = self.get_income(budget.budget_id)
            budget.expenses = self.get_expenses(budget.budget_id)
        return budgets


    def get_income(self, budget_id):
        sql = "SELECT count from cash_flow WHERE budget_id =:budget_id AND is_income = 1;"
        cursor = self.conn.cursor()
        cursor.execute(sql, {"budget_id": budget_id})
        data = cursor.fetchall()
        return [d[0] for d in data]

    def get_expenses(self, budget_id):
        sql = "SELECT count FROM cash_flow WHERE budget_id =:budget_id AND is_income = 0;"
        cursor = self.conn.cursor()
        cursor.execute(sql, {"budget_id": budget_id})
        data = cursor.fetchall()
        return [d[0] for d in data]

    def add_income(self, count, budget_id):
        sql = "INSERT INTO cash_flow (count, is_income_ budget_id)\
            VALUES (:count, 1, :budget_id);"
        cursor = self.conn.cursor()
        cursor.execute(sql, {"count": count, "budget_id": budget_id})
        self.conn.commit()

    def add_expense(self, count, budget_id):
        sql = "INSERT INTO cash_flow (count, is_income_ budget_id)\
            VALUES (:count, 0, :budget_id);"
        cursor = self.conn.cursor()
        cursor.execute(sql, {"count": count, "budget_id": budget_id})
        self.conn.commit()


budget_repository = BudgetRepository(get_database_connection())

if __name__ == "__main__":
    budget_repository.create("test", 1)