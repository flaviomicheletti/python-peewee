from unittest import TestCase
from unittest.mock import patch
from peewee import SqliteDatabase, Model, CharField, IntegerField


class TestFoo(TestCase):
    def test_peewee_crud_read(self):
        # Define a model for testing purposes
        class Person(Model):
            name = CharField()
            age = IntegerField()

        # Patch the `get` method to return a test person
        with patch.object(Person, "get") as mock_get:
            mock_get.return_value = Person(name="Alice", age=30)

            # Call the `get` method and check the returned value
            person = Person.get(Person.name == "Alice")
            assert person.name == "Alice"
            assert person.age == 30
