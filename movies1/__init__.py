from peewee import *

db = SqliteDatabase('movies1.db')

class Movies(Model):
    title = CharField()
    year = IntegerField()
    genre = CharField()

    class Meta:
        database = db


def delete_movie(title):
    try:
        movie = Movies.get(Movies.title == title)
        movie.delete_instance()
        return True
    except Movies.DoesNotExist:
        return False
