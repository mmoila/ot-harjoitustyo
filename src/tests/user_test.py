import unittest
from entities.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user1 = User("user1", "password123")
        self.user2 = User("user2", "password456")

    def set_usernames(self, uname):
        self.user1.username = uname
        self.user2.username = uname + "2"

    def set_passwords(self, pwd):
        self.user1.password = pwd
        self.user2.password = pwd + "2"

    def test_set_username(self):
        self.assertRaises(ValueError, self.set_usernames, "un")
        self.assertRaises(ValueError, self.set_usernames, 7 * "long")
        
        self.set_usernames("user")
        self.assertEqual(self.user1.username, "user")

    def test_set_password(self):
        self.assertRaises(ValueError, self.set_passwords, "short")
        self.assertRaises(ValueError, self.set_passwords, 7 * "long")

        self.set_passwords("ValidPassword")
        self.assertEqual(self.user1.password, "ValidPassword")
        
        
       