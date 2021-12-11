class Budget:
    """Luokka, jonka avulla hallinnoidaan yhtä käyttäjän budjettia.

    Attributes: 
        name = Budjetin nimi.
        budget_id = Budjetin yksilöivä tunniste.
        user_id = Käyttäjän yksilöivä tunniste.
        income = Budjettiin kuuluvat tulot.
        expenses = Budjettiin kuuluvat menot.
    """


    def __init__(self, name, budget_id=None, user_id=None):
        """Luokan konstruktori, joka luo käyttäjälle uuden budjetin.

        Args:
            name: Budjetin nimi.
            budget_id: Budjetin yksilöivä tunniste.. Saa oletuksena arvon None.
            user_id: Käyttäjän yksilöivä tunniste. Saa oletuksena arvon None.
        """

        self.name = name
        self.user_id = user_id
        self.budget_id = budget_id
        self.income = []
        self.expenses = []

    def get_balance(self):
        """Laskee tulojen ja menojen välisen erotuksen.

        Returns:
            Palauttaa tulojen ja menojen välisen erotuksen kahden desimaalin tarkkuudella.
        """
        
        income_sum = sum([income[2] for income in self.income])
        expenses_sum = sum([expense[2] for expense in self.expenses])
        return round(income_sum - expenses_sum, 2)
