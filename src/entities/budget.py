class Budget:
    def __init__(self, name, budget_id=None, user_id=None):
        self.name = name
        self.user_id = user_id
        self.budget_id = budget_id
        self.income = []
        self.expenses = []

    def get_balance(self):
        income_sum = sum([income[2] for income in self.income])
        expenses_sum = sum([expense[2] for expense in self.expenses])
        return round(income_sum - expenses_sum, 2)
