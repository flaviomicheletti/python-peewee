# test_my_database.py
import unittest
from unittest.mock import patch
from peewee import Model, CharField
from conn1 import db


# Mock model
class MockModel(Model):
    name = CharField()

    class Meta:
        database = db

class TestMyDatabase(unittest.TestCase):

    @patch('conn1.SqliteDatabase')
    def test_database_creation(self, mock_sqlite_db):
        # Set up the mock
        mock_instance = mock_sqlite_db.return_value
        mock_instance.connect.return_value = None  # Mock the connect() method

        # Call the code that creates the database
        db.create_tables([MockModel])

