import contextlib
import sqlite3


@contextlib.contextmanager
def connect():
    conn = None
    try:
        conn = sqlite3.connect('query_params_example.sqlite')
        yield conn
    finally:
        if conn is not None:
            conn.close()