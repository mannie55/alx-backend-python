import sqlite3 
import functools

"""your code goes here"""

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('my_database.db')
        print("conn", conn)
        result = func(conn, *args, **kwargs)
        conn.close()
        return result
    return wrapper
    

def transactional(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            conn = args[0]
            conn.execute('BEGIN')
            result = func(*args, **kwargs)
            conn.commit()
            print("result", result)
            print("Transaction committed")
            return result
        except Exception as e:
            conn.rollback()
            print("Rollback!. Error in transaction", e)
            raise e
    return wrapper

@with_db_connection 
@transactional 
def update_user_email(conn, user_id, new_email): 
    cursor = conn.cursor() 
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))
#### Update user's email with automatic transaction handling 

update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')