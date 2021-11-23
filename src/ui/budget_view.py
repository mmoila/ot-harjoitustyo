from tkinter import Tk, constants
from tkinter import ttk


class BudgetView:
    def __init__(self, root, tab, budget):
        self.__root = root
        self.__tab = tab
        self.__budget = budget

        self.__initialize()


    def __initialize(self):
        self.__initialize_income_list()
        self.__initialize_expenses_list()

    def __initialize_income_list(self):
        income_tree = ttk.Treeview(self.__tab, columns=("Type", "Amount"), show="headings")

        for income in self.__budget.income:    
            income_tree.insert("", "end", values=income)

        income_tree.grid(column=0, row=0, sticky=constants.EW)
        
    def __initialize_expenses_list(self):
        expense_tree = ttk.Treeview(self.__tab, columns=("Type", "Amount"), show="headings")

        for expense in self.__budget.expenses:    
            expense_tree.insert("", "end", values=expense)

        expense_tree.grid(column=0, row=2, sticky=constants.EW)