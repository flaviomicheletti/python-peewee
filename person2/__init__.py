from peewee import *

# Create a SQLite database
db = SqliteDatabase("person2.db")

# Define the Person model
class Person(Model):
    name = CharField()
    age = IntegerField()

    class Meta:
        database = db


from peewee import DoesNotExist


def get_person_by_id(person_id: int) -> dict:
    # Connect to the database and retrieve the person
    with db:
        try:
            person = Person.get(Person.id == person_id)
            # Convert the person to a dictionary and return it
            return {"id": person.id, "name": person.name, "age": person.age}
        except DoesNotExist:
            return None
