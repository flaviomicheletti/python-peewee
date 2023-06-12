from peewee import Model, CharField, IntegerField


class Person(Model):
    name = CharField()
    age = IntegerField()
