from tkinter import Tk
from ui.ui import UI


def main():
    window = Tk()
    window.resizable(0, 0)
    window.title("Budgeting app")
    user_interface = UI(window)
    user_interface.start()

    window.mainloop()


if __name__ == "__main__":
    main()
