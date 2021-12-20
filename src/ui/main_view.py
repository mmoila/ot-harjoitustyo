from tkinter import Button, Label, constants, ttk
from tkinter.messagebox import askyesno, showerror
from ui.budget_view import BudgetView
from services.budget_service import budget_service


class MainView:
    def __init__(self, root, logout, user=None):
        self.__root = root
        self.__style = None
        self.__header = None
        self.__top_view = None
        self.__middle_view = None
        self.__user = user
        self.__budgets = None
        self.__logout = logout

        self.__initialize_tabs()

    def __initialize_tabs(self):
        self.__configure_styles()
        self.__create_header()
        self.__create_top_view()
        self.__create_middle_view()
        self.__create_delete_budget_button()

    def destroy(self):
        self.__header.destroy()
        self.__top_view.destroy()
        self.__middle_view.destroy()

    def pack(self):
        self.__header.pack(fill=constants.BOTH)
        self.__top_view.pack(expand=1, pady=20, padx=10, anchor=constants.N)
        self.__middle_view.pack(fill=constants.BOTH, pady=(20, 10), padx=10)

    def __configure_styles(self):
        self.__style = ttk.Style()
        self.__style.configure("Header.TFrame", background="grey")

    def __create_header(self):
        self.__header = ttk.Frame(self.__root, style="Header.TFrame")
        info_label = Label(
            self.__header, text=f"Signed in as {self.__user.username}")
        logout_button = Button(self.__header, text="Logout",
                               command=lambda: self.__handle_logout())

        info_label.pack(side=constants.LEFT, padx=10, pady=10)
        logout_button.pack(side=constants.RIGHT, padx=10, pady=10)

    def __create_middle_view(self):
        self.__middle_view = ttk.Notebook(self.__root)
        self.__budgets = list(budget_service.get_all_budgets())
        for budget in self.__budgets:
            self.__create_tab(budget)

    def __create_tab(self, budget):
        new_tab = ttk.Frame(self.__middle_view)
        self.__middle_view.add(new_tab, text=budget.name)
        BudgetView(new_tab, budget)

    def __create_top_view(self):
        self.__top_view = ttk.Frame(self.__root)
        new_budget_label = ttk.Label(
            master=self.__top_view, text="Add new budget:")
        budget_name = ttk.Entry(master=self.__top_view)
        create_budget_button = ttk.Button(master=self.__top_view, text="Create budget",
                                          command=lambda: self.__add_new_budget(budget_name.get()))

        new_budget_label.grid(row=0, column=0, padx=5, pady=(0, 5))
        budget_name.grid(row=0, column=1, pady=(0, 5))
        create_budget_button.grid(
            row=0, column=2, padx=5, pady=(0, 5), sticky=constants.E)

    def __create_delete_budget_button(self):
        if self.__budgets:
            delete_button = ttk.Button(self.__top_view, text="Delete budget",
                                       command=lambda: self.__delete_budget())
            delete_button.grid(row=1, column=2, padx=5)

    def __add_new_budget(self, name):
        if budget_service.create_budget(name):
            self.destroy()
            self.__initialize_tabs()
            self.pack()
        else:
            showerror("Incorrect budget name",
                      "Budget name length must be between 1 to 20 characters.")

    def __delete_budget(self):
        answer = askyesno(
            "Delete budget", "Confirm permanently delete this budget?")
        if answer:
            tab_num = self.__middle_view.index("current")
            budget_service.delete_budget(self.__budgets[tab_num])
            self.destroy()
            self.__initialize_tabs()
            self.pack()

    def __handle_logout(self):
        self.destroy()
        self.__logout()
