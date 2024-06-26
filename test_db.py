import unittest
import db_connector
from db_connector import DatabaseManager


class TestDatabase(unittest.TestCase):
    """Class for testing database functionality"""
    
    def setUp(self):
        """Set up a connection before tests"""
        self.my_connection = DatabaseManager()

    def test_instance(self):
        """Test the constructor"""
        self.assertIsInstance(self.my_connection, DatabaseManager)

    def test_login(self):
        """Try to log in as an existing user"""
        email = "nils@mail.com"
        password = "Password1!"
        result = self.my_connection.user_credentials(email, password)
        self.assertTrue(result)

    def test_login_invalid_account(self):
        """Try to log in with an invalid username"""
        email = "doesnotexist@mail.com"
        password = "Password1!"
        result = self.my_connection.user_credentials(email, password)
        self.assertFalse(result)

    def test_login_invalid_password(self):
        """Try to log in with an invalid password"""
        email = "nils@mail.com"
        password = "wrongpassword"
        result = self.my_connection.user_credentials(email, password)
        self.assertFalse(result)

    def test_add_user(self):
        """Try to add a new user"""
        first_name = "Peter"
        last_name = "Petersson"
        email = "petersson@gmail.com"
        password = "Password1!"
        result = self.my_connection.add_user(first_name, last_name, email, password)
        self.assertTrue(result)

    def test_add_existing_user(self):
        """Try to add a new user which has the same email as an already existing user"""
        first_name = "Nils"
        last_name = "Nilsson"
        email = "nils@mail.com"
        password = "Password1!"
        result = self.my_connection.add_user(first_name, last_name, email, password)
        self.assertFalse(result)

    def test_delete_user(self):
        """Try to delete a user and then log in"""
        email = "petersson@gmail.com"
        password = "Password1!"
        # Delete user
        self.my_connection.delete_user(email)
        # # Try to log in again (should not work)
        result = self.my_connection.user_credentials(email, password)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()