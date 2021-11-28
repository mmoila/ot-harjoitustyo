from tkinter import Tk, constants, ttk
from ui.budget_view import BudgetView
from services.budget_service import budget_service


class MainView:
    def __init__(self, root):
        self.__root = root
        self.__top_view = None
        self.__middle_view = None
        self.__budgets = None

        self.__initialize_tabs()

    def __initialize_tabs(self):
        self.__create_top_view()
        self.__create_middle_view()

    def __clear_views(self):
        self.__top_view.destroy()
        self.__middle_view.destroy()

    def __create_middle_view(self):
        self.__middle_view = ttk.Notebook(self.__root)
        self.__budgets = [b for b in budget_service.get_all_budgets()]
        for budget in self.__budgets:
            self.__create_tab(budget)
        self.__middle_view.pack(fill=constants.BOTH, pady=(20, 0), padx=10)

    def __create_tab(self, budget):
        new_tab = ttk.Frame(self.__middle_view)
        self.__middle_view.add(new_tab, text=budget.name)
        BudgetView(self.__root, new_tab, budget)

    def __create_top_view(self):
        self.__top_view = ttk.Frame(self.__root)
        new_budget_label = ttk.Label(
            master=self.__top_view, text="Add new budget:")
        budget_name = ttk.Entry(master=self.__top_view)
        button = ttk.Button(master=self.__top_view, text="Create budget",
                            command=lambda: self.__add_new_budget(budget_name.get()))

        self.__top_view.pack(fill=constants.BOTH, pady=10, padx=10)
        new_budget_label.grid(row=0, column=0, padx=5, pady=(0, 5))
        budget_name.grid(row=0, column=1, pady=(0, 5))
        button.grid(row=0, column=2, padx=5, pady=(0, 5))

    def __add_new_budget(self, name):
        if name != "":
            budget_service.create_budget(name)
            self.__clear_views()
            self.__initialize_tabs()
