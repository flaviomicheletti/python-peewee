from unittest import TestCase
from unittest.mock import patch
from person1 import Person


class TestPerson1b(TestCase):
    def test_peewee_crud_read(self):

        # Patch the `get` method to return a test person
        with patch.object(Person, "get") as mock:
            mock.return_value = Person(name="Alice", age=30)

            # Call the `get` method and check the returned value
            person = Person.get(Person.name == "Alice")
            assert person.name == "Alice"
            assert person.age == 30
