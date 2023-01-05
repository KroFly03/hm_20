from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.movie import MovieDAO


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    director_1 = Director(id=1, name='director_1')
    director_2 = Director(id=2, name='director_2')
    director_3 = Director(id=3, name='director_3')

    director_dao.get_one = MagicMock(return_value=director_1)
    director_dao.get_all = MagicMock(return_value=[director_1, director_2, director_3])
    director_dao.create = MagicMock(return_value=director_1)
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()

    return director_dao


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    genre_1 = Genre(id=1, name='genre_1')
    genre_2 = Genre(id=2, name='genre_2')
    genre_3 = Genre(id=3, name='genre_3')

    genre_dao.get_one = MagicMock(return_value=genre_1)
    genre_dao.get_all = MagicMock(return_value=[genre_1, genre_2, genre_3])
    genre_dao.create = MagicMock(return_value=genre_1)
    genre_dao.update = MagicMock()
    genre_dao.delete = MagicMock()

    return genre_dao


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    movie_1 = Movie(id=1,
                    title='title1',
                    description='description_1',
                    trailer='trailer_1',
                    year=1,
                    rating=1,
                    genre_id=1,
                    director_id=1)
    movie_2 = Movie(id=2,
                    title='title2',
                    description='description_2',
                    trailer='trailer_2',
                    year=2,
                    rating=2,
                    genre_id=2,
                    director_id=2)
    movie_3 = Movie(id=3,
                    title='title3',
                    description='description_3',
                    trailer='trailer_3',
                    year=3,
                    rating=3,
                    genre_id=3,
                    director_id=3)

    movie_dao.get_one = MagicMock(return_value=movie_1)
    movie_dao.get_all = MagicMock(return_value=[movie_1, movie_2, movie_3])
    movie_dao.create = MagicMock(return_value=movie_1)
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()

    return movie_dao
