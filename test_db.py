import unittest
import db_connector
from db_connector import DatabaseManager

"""Class for testing database functionality"""
class TestDatabase(unittest.TestCase):
    
    def test_login(self):
        """Try to log in as an existing user"""
        my_connection = DatabaseManager()
        email = "nils@mail.com"
        password = "Password1!"
        result = my_connection.user_credentials(email, password)
        self.assertTrue(result)

    def test_login_invalid_account(self):
        """Try to log in as an existing user"""
        my_connection = DatabaseManager()
        email = "doesnotexist@mail.com"
        password = "Password1!"
        result = my_connection.user_credentials(email, password)
        self.assertFalse(result)

    def test_login_invalid_password(self):
        """Try to log in with an invalid password"""
        my_connection = DatabaseManager()
        email = "nils@mail.com"
        password = "wrongpassword"
        result = my_connection.user_credentials(email, password)
        self.assertFalse(result)

    def test_add_user(self):
        """Try to add a new user"""
        my_connection = DatabaseManager()
        first_name = "Peter"
        last_name = "Petersson"
        email = "petersson@gmail.com"
        password = "Password1!"
        result = my_connection.add_user(first_name, last_name, email, password)
        self.assertTrue(result)

    def test_add_existing_user(self):
        """Try to add a new user which has the same email as an already existing user"""
        my_connection = DatabaseManager()
        first_name = "Nils"
        last_name = "Nilsson"
        email = "nils@mail.com"
        password = "Password1!"
        result = my_connection.add_user(first_name, last_name, email, password)
        self.assertFalse(result)

    def test_delete_user(self):
        """Try to delete a user and then log in"""
        my_connection = DatabaseManager()
        email = "petersson@gmail.com"
        password = "Password1!"
        #Delete user
        my_connection.delete_user(email)
        #Try to log in again (should not work)
        result = my_connection.user_credentials(email, password)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()