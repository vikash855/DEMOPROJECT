import mysql.connector

db_connection = mysql.connector.connect(host='localhost',
                                        database='djangosql',
                                        user='root',
                                        password='12345')
db_cursor = db_connection.cursor()

