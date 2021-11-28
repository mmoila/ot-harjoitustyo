from tkinter import Tk
from ui.ui import UI


def main():
    window = Tk()
    window.minsize(height=800, width=450)
    window.title("Budgeting app")
    ui = UI(window)
    ui.start()

    window.mainloop()


if __name__ == "__main__":
    main()
