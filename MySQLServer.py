import mysql.connector

try:
    connection = mysql.connector.connect(host="localhost", user="root", password="pass")
    create_db_query = "CREATE DATABASE alx_book_store"
    my_cursor = connection.cursor()
    my_cursor.execute(create_db_query)
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print("Error occured: " + e)
    
finally:
    my_cursor.close()
    connection.close()
