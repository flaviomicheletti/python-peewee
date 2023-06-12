from peewee import Model, CharField, IntegerField
from person3.conn import db


# Define the Person model
class Person(Model):
    name = CharField()
    age = IntegerField()

    class Meta:
        database = db
