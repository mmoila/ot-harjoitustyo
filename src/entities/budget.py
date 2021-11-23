class Budget:
    def __init__(self, name, budget_id=None, user_id=None):
        self.name = name
        self.user_id = user_id
        self.budget_id = budget_id
        self.income = []
        self.expenses = []
        

    def get_balance(self):
        return (sum(self.income) - sum(self.expenses))