import pymysql


def stream_users_in_ages():
    # Connect to the database
    mydb = pymysql.connect(
        host="localhost",
        user="root",
        password="5545851170",
        database="ALX_prodev" 
    )

    mycursor = mydb.cursor(pymysql.cursors.DictCursor)
    mycursor.execute("SELECT age FROM user_data")
    
    for user_age in mycursor:
        yield user_age

def calculate_average_age():
    total_age = 0
    count = 0
    for user_age in stream_users_in_ages():
        total_age += user_age['age']
        count += 1
    print(total_age)
    print(f"Average age of users: {total_age / count}")



calculate_average_age()
