import sqlite3

class ExecuteQuery:
    def __init__(self, query, params=None):
        self.query = query
        self.params = params
        self.conn = None
        self.results = None

    def __enter__(self):
        self.conn = sqlite3.connect('my_database.db')
        cursor = self.conn.cursor()

        if self.params:
            cursor.execute(self.query, self.params)
        else:
            cursor.execute(self.query)

        self.results = cursor.fetchall()
        return self.results  # This will be available in the `with` block

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()
            print("Connection closed.")

# ✅ Example usage:
query = "SELECT * FROM users WHERE age > ?"
params = (25,)

with ExecuteQuery(query, params) as result:
    print("Query Results:")
    for row in result:
        print(row)
