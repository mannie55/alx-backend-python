import time
import sqlite3 
import functools

#### paste your with_db_decorator here

def with_db_connection(func):
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('my_database.db')
        result = func(conn, *args, **kwargs)
        conn.close()
        return result
    return wrapper

def retry_on_failure(retries=3, delay=1):
    # define the decorator
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {i+1} failed: {e}")
                    time.sleep(delay)
            raise Exception("Sory all attempts failed")
        return wrapper
    return decorator

@with_db_connection
@retry_on_failure(retries=3, delay=1)

def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)