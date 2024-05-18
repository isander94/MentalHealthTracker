import unittest
from datetime import datetime
from db_connector import DatabaseManager


class TestDatabase(unittest.TestCase):
    """Class for testing database functionality"""

    def setUp(self):
        """Set up a connection before tests"""
        self.my_connection = DatabaseManager()

    def tearDown(self):
        self.my_connection.close_connection()

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

    def test_add_note(self):
        """Try to add a note to the database"""
        note = "This is a test note"
        result = self.my_connection.add_note(note, "nils@mail.com")
        self.assertTrue(result)

    def test_add_note_invalid_account(self):
        """Try to add a note to the database with an account that is invalid"""
        note = "This is a test note"
        result = self.my_connection.add_note(note, "doesnotexist@mail.com")
        self.assertFalse(result)

    def test_get_note(self):
        """Try to fetch a note associated with a user"""
        email = "nils@mail.com"
        expected_note = "This is a test note 2024-05-13"
        result = self.my_connection.previous_notes(email)
        note = result[0][0] + " " + result[0][1].strftime("%Y-%m-%d")
        self.assertEqual(expected_note, note)


if __name__ == "__main__":
    unittest.main()