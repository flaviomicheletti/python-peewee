from peewee import SqliteDatabase, Model, CharField, IntegerField


class Person(Model):
    name = CharField()
    age = IntegerField()
