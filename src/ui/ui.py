from ui.main_view import MainView


class UI: 
    def __init__(self, root):
        self.__root = root 
        self.__current_view = None

    def start(self):
        self.__show_main_view()
        
    def __show_main_view(self):
        self.__current_view = MainView(self.__root)
       