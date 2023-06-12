# Peewee

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

