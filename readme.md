

# Instalation

__venv:__

    python3 -m venv .venv && . .venv/bin/activate

## Install

In both environments you will need to install it only once.

    // in the first time
    pip install -U pytest
    pip install pytest-mock
    pip install pytest-cov
    pip install coverage
    pip install requests
    pip install SQLAlchemy
    pip install psycopg2

## Running

    pytest


## Coverage

    coverage run -m pytest
    coverage html

    pytest --cov . --cov-report html


## Running

    python -m unittest discover -v
    python -m unittest discover -p 'test_*.py'


## Coverage

    coverage run -m unittest discover
    coverage report -m
    coverage html
