from tkinter import ttk
from tkinter.messagebox import showerror, showinfo
from typing import Text
from services.budget_service import budget_service, UserNameExistsError

class LoginView:
    def __init__(self, root, login_success):
        self.__root = root
        self.__login_success = login_success
        self.__login_frame = None
        self.__new_user_frame = None
        self.__username_entry = None
        self.__password_entry = None
        self.__initialize()

    def pack(self):
        if self.__login_frame:
            self.__login_frame.pack(pady=(40), padx=60)
        if self.__new_user_frame:
            self.__new_user_frame.pack()

    def destroy(self):
        if self.__login_frame:
            self.__login_frame.destroy()
        if self.__new_user_frame:
            self.__new_user_frame.destroy()

    def __initialize(self):
        self.__login_frame = ttk.Frame(self.__root)
        self.__initialize_username_field(self.__login_frame)
        self.__initialize_password_field(self.__login_frame)
        self.__initialize_login_button(self.__login_frame)
        self.__initialize_create_user_button(self.__login_frame)

    def __initialize_username_field(self, master):
        username_label = ttk.Label(master, text="Username")
        self.__username_entry = ttk.Entry(master)
        username_label.pack()
        self.__username_entry.pack(pady=10)

    def __initialize_password_field(self, master):
        password_label = ttk.Label(master, text="Password")
        self.__password_entry = ttk.Entry(master)
        password_label.pack()
        self.__password_entry.pack(pady=10)

    def __initialize_login_button(self, master):
        login_button = ttk.Button(master, text="Login",
                                  command=lambda: self.__handle_login())
        login_button.pack()

    def __handle_login(self):
        username = self.__username_entry.get()
        password = self.__password_entry.get()
        if budget_service.login(username, password):
            self.__login_success()
        else:
            showerror(title="Login error", message="Incorrect username or password")
            self.__login_frame.destroy()
            self.__initialize()
            self.pack()

    def __create_user(self):
        username = self.__username_entry.get()
        password = self.__password_entry.get()
        try:
            budget_service.create_user(username, password)
        except ValueError as error:
            showerror(title="Login error", message=error)
        except UserNameExistsError as error:
            showerror(title="Login error", message=error)
        else: 
            showinfo(title="New user", message="New user created succesfully!")
            self.__login_frame.destroy()
            self.__initialize()
            self.pack()

    def __initialize_create_user_button(self, master):
        create_user_button = ttk.Button(master, text="Create user", 
                                        command=lambda: self.__create_user())
        create_user_button.pack(pady=(25, 0))