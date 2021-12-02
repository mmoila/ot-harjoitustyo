from os import read
from tkinter import ttk, constants
from typing import Text
from unittest.loader import makeSuite
from services.budget_service import budget_service

def add_placeholder(entry, txt):
    entry.insert(0, txt)
    entry.bind("<Button-1>", lambda *args: entry.delete(0, "end"))


class BudgetView:
    def __init__(self, tab, budget):
        self.__tab = tab
        self.__frame = None
        self.__budget = budget
        self.__income_tree = None
        self.__expense_tree = None
        self.__initialize()

    def __initialize(self):
        self.__initialize_frame()
        self.__initialize_income_list()
        self.__initialize_new_income()
        self.__initialize_expenses_list()
        self.__initialize_new_expense()
        self.__initialize_budget_balance()

    def __initialize_frame(self):
        if self.__frame:
            self.__frame.destroy()
        self.__frame = ttk.Frame(self.__tab)
        self.__frame.pack()

    def __initialize_income_list(self):
        self.__income_tree = ttk.Treeview(
            self.__frame, columns=("id", "Description", "Amount"), show="")

        for income in self.__budget.income:
            self.__income_tree.insert("", "end", values=income)

        self.__income_tree["displaycolumns"] = ("Description", "Amount")
        self.__income_tree.pack(fill=constants.X, pady=(25, 0))

    def __initialize_expenses_list(self):
        self.__expense_tree = ttk.Treeview(
            self.__frame, columns=("id", "Description", "Amount"), show="")

        for expense in self.__budget.expenses:
            self.__expense_tree.insert("", "end", values=expense)

        self.__expense_tree["displaycolumns"] = ("Description", "Amount")
        self.__expense_tree.pack(fill=constants.X, pady=(25, 0))

    def __initialize_new_income(self):
        container = ttk.Frame(self.__frame)
        label = ttk.Label(container, text="New income:")
        description = ttk.Entry(container)
        amount = ttk.Entry(container, width=10)
        add_new_button = ttk.Button(container, text="Add new",
                            command=lambda: self.__add_income(description.get(),
                                                              amount.get(), self.__budget))
        delete_button = ttk.Button(container, text="Delete selection",
                                   command=lambda: self.__delete_income())

        add_placeholder(description, "Description")
        add_placeholder(amount, "Amount")
        container.pack(padx=5, pady=5)
        label.grid(row=0, column=0, padx=5)
        description.grid(row=0, column=1)
        amount.grid(row=0, column=2, padx=5)
        add_new_button.grid(row=0, column=3)
        delete_button.grid(row=1, column=0, padx=5, pady=5)

    def __initialize_new_expense(self):
        container = ttk.Frame(self.__frame)
        label = ttk.Label(container, text="New expense:")
        description = ttk.Entry(container)
        amount = ttk.Entry(container, width=10)
        add_new_button = ttk.Button(container, text="Add new",
                            command=lambda: self.__add_expense(description.get(),
                                                               amount.get(), self.__budget))
        delete_button = ttk.Button(container, text="Delete selection",
                                   command=lambda: self.__delete_expense())

        add_placeholder(description, "Description")
        add_placeholder(amount, "Amount")
        container.pack(padx=5, pady=5)
        label.grid(row=0, column=0, padx=5)
        description.grid(row=0, column=1)
        amount.grid(row=0, column=2, padx=5)
        add_new_button.grid(row=0, column=3)
        delete_button.grid(row=1, column=0, padx=5, pady=5)

    def __initialize_budget_balance(self):
        balance = self.__budget.get_balance()
        label = ttk.Label(
            self.__frame, text=f"Budget balance: {balance} €", font="bold")

        label.pack(pady=40, padx=10, side=constants.LEFT)

    def __add_income(self, description, amount, budget):
        budget_service.add_budget_income(description, amount, budget)
        self.__budget = budget_service.get_budget(self.__budget.budget_id)
        self.__initialize()

    def __add_expense(self, description, amount, budget):
        budget_service.add_budget_expense(description, amount, budget)
        self.__budget = budget_service.get_budget(self.__budget.budget_id)
        self.__initialize()

    def __delete_income(self):
        ids = []
        rows = self.__income_tree.selection()
        for row in rows:
            values = self.__income_tree.item(row)["values"]
            ids.append(values[0])
        for budget_id in ids:
            budget_service.delete_budget_income(budget_id)
        self.__budget = budget_service.get_budget(self.__budget.budget_id)
        self.__initialize()

    def __delete_expense(self):
        ids = []
        rows = self.__expense_tree.selection()
        for row in rows:
            values = self.__expense_tree.item(row)["values"]
            print(values)
            ids.append(values[0])
        for budget_id in ids:
            budget_service.delete_budget_expense(budget_id)
        self.__budget = budget_service.get_budget(self.__budget.budget_id)
        self.__initialize()
