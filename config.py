import sys
import mysql.connector
from cryptography.fernet import Fernet
from pass_gen import generate_master_password


def connect():
    # Connect to database
    try:
        connection = mysql.connector.connect(
            host='przytop.mysql.pythonanywhere-services.com',  # Host name, default is localhost/127.0.0.1
            user='przytop',  # Your mysql root name <---------------- EDIT HERE EDIT HERE EDIT HERE
            password='xL9rb8X6*X70',  # Enter your password here <---------------- EDIT HERE EDIT HERE EDIT HERE
        )
        return connection
    except (Exception, mysql.connector.Error) as e:
        print(e)
        return 'error'


def install():
    db = connect()
    cursor = db.cursor()
    # Create a database
    try:
        cursor.execute('CREATE DATABASE passcode')
        print("Database 'passcode' created")
    except Exception as e:
        print(f'An error occurred while trying to create database\n{e}\nProgram exiting')
        cursor.close()
        db.close()
        sys.exit(0)

    # Create tables
    query = f'CREATE TABLE passcode.master (master_key_hash TEXT NOT NULL)'  # Master password here
    query2 = f'CREATE TABLE passcode.secret (secret_key TEXT NOT NULL)'  # Secret key here
    query3 = f'CREATE TABLE passcode.entries (website TEXT, email TEXT, password TEXT)'  # All your entries here
    cursor.execute(query)
    cursor.execute(query2)
    cursor.execute(query3)
    print('Table entries created')

    # Create master password and hash it
    val = (generate_master_password(),)

    # Create secret key
    val2 = (Fernet.generate_key(),)

    # Add them to database
    query = 'INSERT INTO passcode.master (master_key_hash) VALUES (%s)'
    query2 = 'INSERT INTO passcode.secret (secret_key) VALUES (%s)'
    cursor.execute(query, val)
    cursor.execute(query2, val2)
    db.commit()
    print('Added to the database')
    print('Configuration completed')
    cursor.close()
    db.close()


def delete():
    db = connect()
    cursor = db.cursor()
    # Delete a passcode database
    try:
        cursor.execute('DROP DATABASE passcode')
        print("Database 'passcode' deleted")
    except Exception as e:
        print(f'An error occurred while trying to delete database\n{e}')
    cursor.close()
    db.close()


def reinstall():
    # First delete, then install again
    delete()
    install()


def check_database():
    db = connect()
    cursor = db.cursor()
    # Check if a database exists
    query = "SHOW DATABASES LIKE 'passcode'"
    cursor.execute(query)
    return cursor.fetchone()
