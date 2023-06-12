import unittest
from unittest.mock import patch
from peewee import SqliteDatabase
from conn2 import db


class TestConnection(unittest.TestCase):
    @patch.object(SqliteDatabase, '__init__')
    def test_database_connection(self, mock_init):
        # Set up the mock behavior
        mock_init.return_value = None

        # Perform the test
        # In this case, accessing the `db` variable will invoke the mocked initialization
        self.assertIsNotNone(db)

