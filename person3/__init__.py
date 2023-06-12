from peewee import DoesNotExist
from person3.conn import db
from person3.models import Person


def get_person_by_id(person_id: int) -> dict:
    # Connect to the database and retrieve the person
    with db:
        try:
            person = Person.get(Person.id == person_id)
            # Convert the person to a dictionary and return it
            return {"id": person.id, "name": person.name, "age": person.age}
        except DoesNotExist:
            return None
