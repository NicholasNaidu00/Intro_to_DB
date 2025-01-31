import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Connect to MySQL server
        conn = mysql.connector.connect(
            host='localhost',
            user='your_username',    # Replace with your MySQL username
            password='your_password' # Replace with your MySQL password
        )

        # Create a cursor object
        cursor = conn.cursor()

        # Create database if it does not exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        # Print success message
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your username and password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print(f"Error: {err}")
    
    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()

if __name__ == "__main__":
        create_database()
