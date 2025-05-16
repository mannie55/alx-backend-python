import pymysql


def paginate_users(page_size, offset):
    mydb = pymysql.connect(
        host="localhost",
        user="root",  # or the correct DB user
        password="5545851170",  # change to your real password
        database="ALX_prodev"  # replace with your DB name
    )

    mycursor = mydb.cursor(pymysql.cursors.DictCursor)
    mycursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return rows

def lazy_pagination(page_size):
    offset = 0
    while True:
        users = paginate_users(page_size, offset)
        if not users:
            break
        yield users
        offset += page_size
        break