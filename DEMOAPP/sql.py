import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='djangosql',
                                         user='root',
                                         password='12345')

    if connection.is_connected():
        db_info = connection.get_server_info()
        print("connection to my sql version", db_info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("u r connected to database:", record)

except Error as e:
    print("error while connecting to MySQL", e)
