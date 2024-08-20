import unittest
import re
from unittest.mock import patch
from io import StringIO

class TestUserInputValidation(unittest.TestCase):

    def test_get_username_valid(self):
        with patch('builtins.input', return_value="JohnDoe123"):
            self.assertEqual(get_username(), "JohnDoe123")

    def test_get_username_invalid(self):
        with patch('builtins.input', return_value="John_Doe"):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                get_username()
                self.assertEqual(mock_stdout.getvalue().strip(), "Invalid username. Only alphanumeric characters and underscores are allowed.")

    def test_get_username_unexpected(self):
        with patch('builtins.input', return_value="John@Doe"):
            self.assertIsNone(get_username())

    def test_get_password_valid(self):
        with patch('builtins.input', return_value="StrongPassword"):
            self.assertEqual(get_password(), "StrongPassword")

    def test_get_password_invalid(self):
        with patch('builtins.input', return_value="Weak"):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                get_password()
                self.assertEqual(mock_stdout.getvalue().strip(), "Invalid password. It must be at least 8 characters long.")

    def test_get_password_unexpected(self):
        with patch('builtins.input', return_value="Short"):
            self.assertIsNone(get_password())

    def test_get_email_valid(self):
        with patch('builtins.input', return_value="test@example.com"):
            self.assertEqual(get_email(), "test@example.com")

    def test_get_email_invalid(self):
        with patch('builtins.input', return_value="invalid_email"):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                get_email()
                self.assertEqual(mock_stdout.getvalue().strip(), "Invalid email address format.")

    def test_get_email_unexpected(self):
        with patch('builtins.input', return_value="test[at]example.com"):
            self.assertIsNone(get_email())

    def test_get_sql_query_valid(self):
        with patch('builtins.input', return_value="SELECT * FROM users"):
            self.assertEqual(get_sql_query(), "SELECT * FROM users")

    def test_get_sql_query_invalid(self):
        with patch('builtins.input', return_value="DROP TABLE users"):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                get_sql_query()
                self.assertEqual(mock_stdout.getvalue().strip(), "Invalid query. Destructive operations are not allowed.")

    def test_get_sql_query_unexpected(self):
        with patch('builtins.input', return_value="DELETE FROM users"):
            self.assertIsNone(get_sql_query())

if __name__ == '__main__':
    unittest.main()

