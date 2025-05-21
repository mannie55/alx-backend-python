import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        # makes connection available to the with block
        return self.connection
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.close()
# use context manager to fetch user data from database
with DatabaseConnection('my_database.db') as db_connection:
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    print(users)