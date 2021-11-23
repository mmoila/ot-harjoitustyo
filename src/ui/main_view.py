from tkinter import Tk, constants, ttk
from ui.budget_view import BudgetView
from services.budget_service import budget_service

class MainView:
    def __init__(self, root):
        self.__root = root
        self.__tab_control = None
        self.__budgets = None

        self.__initialize_tabs()
        

    def __initialize_tabs(self):
        self.__tab_control = ttk.Notebook(self.__root)
        self.__budgets = [b for b in budget_service.get_all_budgets()]
        for budget in self.__budgets:
            self.__create_tab(budget)
        self.__tab_control.grid(row=1)
        self.__create_new_budget_frame()
        self.__root.grid_columnconfigure(1, weight=1)

    def __create_tab(self, budget):
        new_tab = ttk.Frame(self.__tab_control)
        self.__tab_control.add(new_tab, text=budget.name)
        budget = BudgetView(self.__root, new_tab, budget)

    def __create_new_budget_frame(self):
        frame = ttk.Frame(self.__root)
        new_budget_label = ttk.Label(master=frame, text="Budget name")
        budget_name = ttk.Entry(master=frame)
        button = ttk.Button(master=frame, text="Create budget",
                            command=lambda: self.__add_new_budget(budget_name.get()))

        frame.grid(row=0, sticky=constants.EW, pady=(10, 20))
        new_budget_label.grid(row=0, column=0, padx=5, pady=(0, 5))
        budget_name.grid(row=0, column=1, pady=(0, 5))
        button.grid(row=0, column=2, padx=5, pady=(0, 5))

    def __add_new_budget(self, name):
        if name != "":
            budget_service.create_budget(name)
            self.__initialize_tabs()
      