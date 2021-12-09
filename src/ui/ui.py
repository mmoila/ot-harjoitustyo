from ui.main_view import MainView
from ui.login_view import LoginView


class UI:
    def __init__(self, root):
        self.__root = root
        self.__active_view = None

    def start(self):
        self.__show_login_view()

    def __show_main_view(self, user):
        self.__active_view.destroy()
        self.__active_view = MainView(self.__root, self.__show_login_view, user)
        for i in range(3):
            self.__root.columnconfigure(i, weight=1, minsize=50)
            self.__root.rowconfigure(i, weight=1, minsize=50)
        self.__active_view.pack()

    def __show_login_view(self):
        self.__active_view = LoginView(self.__root, self.__show_main_view)
        self.__active_view.pack()
