import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def test_user_attributes(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_str_representation(self):
        user = User()
        user.email = "dave@gmail.com"
        user.first_name = "Dave"
        user.last_name = "Pare"
        expected_str = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(str(user), expected_str)

    def test_user_instance(self):
        user = User()
        self.assertIsInstance(user, User)

    def test_user_id_generation(self):
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_user_creation_with_attributes(self):
        user = User(
            email="dave@gmail.com",
            password="12345",
            first_name="Dave",
            last_name="Pare")
        self.assertEqual(user.email, "dave@gmail.com")
        self.assertEqual(user.password, "12345")
        self.assertEqual(user.first_name, "Dave")
        self.assertEqual(user.last_name, "Pare")

    def test_user_id_is_string(self):
        user = User()
        self.assertIsInstance(user.id, str)


if __name__ == '__main__':
    unittest.main()
