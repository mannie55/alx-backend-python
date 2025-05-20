import time
import sqlite3 
import functools


query_cache = {}

"""your code goes here"""

def with_db_connection(func):
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('my_database.db')
        result = func(conn, *args, **kwargs)
        conn.close()
        return result
    return wrapper

def cache_query(func):
    @functools.lru_cache(maxsize=None)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('before execution')
        print('after execution')
        return result
    return wrapper





@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")