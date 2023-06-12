import unittest
from unittest.mock import patch
from movies1 import Movies, delete_movie
from peewee import SqliteDatabase


class TestDeleteMovie(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Use an in-memory database for testing
        db = SqliteDatabase(':memory:')
        Movies._meta.database = db
        Movies.create_table()

    @classmethod
    def tearDownClass(cls):
        # Drop the Movies table and close the database connection
        Movies.drop_table()
        Movies._meta.database.close()

    def test_delete_existing_movie(self):
        # Create a movie to delete
        movie = Movies.create(title='The Godfather', year=1972, genre='Crime')

        # Call delete_movie with the movie's title
        with patch('movies1.Movies.get') as mock_get:
            mock_get.return_value = movie
            result = delete_movie('The Godfather')

        # Check that the movie was deleted and the function returned True
        self.assertTrue(result)
        self.assertFalse(Movies.select().where(
            Movies.title == 'The Godfather').exists())

    def test_delete_nonexistent_movie(self):
        # Call delete_movie with a title that doesn't exist
        with patch('movies1.Movies.get') as mock_get:
            mock_get.side_effect = Movies.DoesNotExist
            result = delete_movie('Nonexistent Movie')

        # Check that no movie was deleted and the function returned False
        self.assertFalse(result)
        self.assertFalse(Movies.select().where(
            Movies.title == 'Nonexistent Movie').exists())
