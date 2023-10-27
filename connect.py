import psycopg2
from contextlib import contextmanager

@contextmanager
def create_connection():
    try:
        conn = psycopg2.connect(host = 'localhost', database = 'school', user = 'postgres', password = 'mikel')
        yield conn
        conn.close()
    except psycopg2.OperationalError as e:
        raise RuntimeError(f'Could not connect to database {e}')