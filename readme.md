![image](https://github.com/flaviomicheletti/python-peewee/assets/1257048/dcadd9a8-0443-41fb-9274-326f301cd0db)

Peewee is a simple and small ORM. It has few (but expressive) concepts,
making it easy to learn and intuitive to use.

- https://docs.peewee-orm.com/en/latest/
- https://pypi.org/project/peewee/
- https://github.com/coleifer/peewee

__venv:__

    python3 -m venv .venv && . .venv/bin/activate

__Running:__

    python -m unittest discover -v
    python -m unittest discover -p 'test_*.py'

__Coverage:__

    coverage run -m unittest discover

    coverage report -m
    coverage html

    coverage run -m unittest discover &&  coverage html

