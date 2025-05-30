import pymysql

def stream_users_in_batches(batch_size=100):
    # Connect to the database
    mydb = pymysql.connect(
        host="localhost",
        user="root",
        password="5545851170",
        database="ALX_prodev" 
    )

    mycursor = mydb.cursor(pymysql.cursors.DictCursor)
    mycursor.execute("SELECT * FROM user_data")

    while True:
        users = mycursor.fetchmany(batch_size)
        if not users:
            break
        yield users
    mycursor.close()
    mydb.close()

def batch_processing(batch_size=100):
    for users in stream_users_in_batches(batch_size):
        for user in users:
            if user['age'] > 25:
                print(user)
        break
    return user
