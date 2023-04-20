from contextlib import contextmanager
import mysql.connector

# Define a context manager for the database connection and cursor
@contextmanager
def my_sql_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="bigdata",
        database="personal_crm"
    )
    c = mydb.cursor()
    try:
        yield c
        mydb.commit()
    except Exception as e:
        mydb.rollback()
        raise e
    finally:
        c.close()
        mydb.close()