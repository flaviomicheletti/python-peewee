from unittest import TestCase
from unittest.mock import patch
from foo01 import Person


class TestFoo(TestCase):
    def test_peewee_crud_read(self):

        # Patch the `get` method to return a test person
        with patch.object(Person, "get") as mock_get:
            mock_get.return_value = Person(name="Alice", age=30)

            # Call the `get` method and check the returned value
            person = Person.get(Person.name == "Alice")
            assert person.name == "Alice"
            assert person.age == 30
