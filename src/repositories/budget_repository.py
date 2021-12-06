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

    def delete_budget(self, budget):
        sql = "DELETE FROM budgets WHERE id = :id"
        cursor = self.conn.cursor()
        cursor.execute(sql, {"id": budget.budget_id})
        self.conn.commit()

    def get_all_budgets(self, user_id):
        sql = "SELECT id, name, user_id from budgets WHERE user_id=:user_id;"
        cursor = self.conn.cursor()
        cursor.execute(sql, {"user_id": user_id})
        rows = cursor.fetchall()
        budgets = list(map(get_budgets_by_rows, rows))
        for budget in budgets:
            budget.income = self.get_income(budget.budget_id)
            budget.expenses = self.get_expenses(budget.budget_id)
        return budgets

    def get_budget(self, id_):
        sql = "SELECT id, name, user_id FROM budgets WHERE id=:id"
        cursor = self.conn.cursor()
        cursor.execute(sql, {"id": id_})
        row = cursor.fetchone()
        budget = Budget(row["name"], row["id"], row["user_id"])
        budget.income = self.get_income(budget.budget_id)
        budget.expenses = self.get_expenses(budget.budget_id)
        return budget

    def get_income(self, budget_id):
        sql = "SELECT id, description, count from cash_flow\
            WHERE budget_id =:budget_id AND is_income = 1;"
        cursor = self.conn.cursor()
        cursor.execute(sql, {"budget_id": budget_id})
        data = cursor.fetchall()
        return [(d[0], d[1], d[2]) for d in data]

    def get_expenses(self, budget_id):
        sql = "SELECT id, description, count FROM cash_flow\
            WHERE budget_id =:budget_id AND is_income = 0;"
        cursor = self.conn.cursor()
        cursor.execute(sql, {"budget_id": budget_id})
        data = cursor.fetchall()
        return [(d[0], d[1], d[2]) for d in data]

    def add_income(self, description, count, budget_id):
        sql = "INSERT INTO cash_flow (description, count, is_income, budget_id)\
            VALUES (:description, :count, 1, :budget_id);"
        cursor = self.conn.cursor()
        cursor.execute(sql, {"description": description,
                       "count": count, "budget_id": budget_id})
        self.conn.commit()

    def add_expense(self, description, count, budget_id):
        sql = "INSERT INTO cash_flow (description, count, is_income, budget_id)\
            VALUES (:description, :count, 0, :budget_id);"
        cursor = self.conn.cursor()
        cursor.execute(sql, {"description": description,
                       "count": count, "budget_id": budget_id})
        self.conn.commit()

    def delete_cash_flow(self, id_, is_income):
        sql = "DELETE FROM cash_flow WHERE id=:id AND is_income =:is_income;"
        cursor = self.conn.cursor()
        cursor.execute(sql, {"id": id_, "is_income": is_income})
        self.conn.commit()

    def delete_all(self):
        sql = "DELETE FROM budgets;\
               DELETE FROM cash_flow;"
        cursor = self.conn.cursor()
        cursor.executescript(sql)
        self.conn.commit()


budget_repository = BudgetRepository(get_database_connection())

if __name__ == "__main__":
    budget_repository.create("test", 1)
