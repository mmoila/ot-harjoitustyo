import unittest
from repositories.user_repository import user_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user1 = User(username="user1", password="test1234")
        self.user2 = User(username="user2", password="test5678")

    def test_create_user(self):
        user_repository.create_user(self.user1)
        user = user_repository.get_user("user1", "test1234")

        self.assertEqual(user.username, "user1")
        self.assertEqual(user.password, "test1234")

    def test_get_nonexistent_user(self):
        user = user_repository.get_user("Pekka", "test1234")

        self.assertIsNone(user)

    def test_check_user(self):
        user_repository.create_user(self.user1)

        self.assertTrue(user_repository.check_user("user1"))
        self.assertFalse(user_repository.check_user("user2"))
