# import mysql.connector


# def stream_users():
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="5545851170",
#         database="ALX_prodev"
#     )
#     mycursor = mydb.cursor()
#     mycursor.execute("SELECT * FROM user_data")

#     for user in mycursor:
#         yield user

#     mycursor.close()
#     mydb.close()

import pymysql

def stream_users():
    # Connect to the database
    mydb = pymysql.connect(
        host="localhost",
        user="root",
        password="5545851170",
        database="ALX_prodev"
    )

    mycursor = mydb.cursor(pymysql.cursors.DictCursor)
    mycursor.execute("SELECT * FROM user_data")

    # Loop through results and yield one row at a time
    for row in mycursor:
        yield row

    # Optional: close resources (will close after generator is exhausted)
    mycursor.close()
    mydb.close()
