class User:
    def __init__(self, username, password, id=None):
        self.id = id
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @username.setter
    def username(self, username):
        if len(username) < 4 or len(username) > 20:
            raise ValueError("Username length must be between 4 and 20.")
        self.__username = username
    
    @password.setter
    def password(self, password):
        if len(password) < 8 or len(password) > 25:
            raise ValueError ("Password length must be between 8 and 25.")
        self.__password = password
        

   