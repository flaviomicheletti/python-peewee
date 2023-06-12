import unittest
from unittest.mock import patch
from peewee import DoesNotExist
from person3 import get_person_by_id, Person

class TestPerson2(unittest.TestCase):
    def test_existing_person(self):
        # Create a mock person with ID 1
        mock_person = Person(id=1, name='Alice', age=25)

        # Mock the Person.get method to return the mock person
        with patch.object(Person, 'get', return_value=mock_person):
            # Call the get_person_by_id function with ID 1
            result = get_person_by_id(1)

            # Assert that the result is a dictionary with the expected values
            self.assertDictEqual(result, {'id': 1, 'name': 'Alice', 'age': 25})

    def test_nonexistent_person(self):
        # Mock the Person.get method to raise a DoesNotExist exception
        with patch.object(Person, 'get', side_effect=DoesNotExist):
            # Call the get_person_by_id function with ID 1
            result = get_person_by_id(1)

            # Assert that the result is None
            self.assertIsNone(result)
