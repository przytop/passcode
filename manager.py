from config import connect
from pass_gen import encrypt, decrypt


def get_key(key, column):
    db = connect()
    cursor = db.cursor()
    # Get key from database
    try:
        select_query = f"SELECT {key} FROM passcode.{column}"
        cursor.execute(select_query)
        return cursor.fetchone()[0]
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.close()


def add_entry(website, email, password):
    db = connect()
    cursor = db.cursor()
    # Add entry to database
    try:
        insert_query = f'INSERT INTO passcode.entries (website, email, password) VALUES (%s, %s, %s)'
        val = (
            website,
            encrypt(get_key('secret_key', 'secret'), email),
            encrypt(get_key('secret_key', 'secret'), password)
        )
        cursor.execute(insert_query, val)
        db.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.close()


def search_entry(search):
    db = connect()
    cursor = db.cursor()
    # Search entry from database
    try:
        select_query = f"SELECT * FROM passcode.entries WHERE website = '{search}'"
        cursor.execute(select_query)
        records = cursor.fetchall()
        return records
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.close()


def del_entry(search):
    db = connect()
    cursor = db.cursor()
    # Delete entry from database
    try:
        select_query = f"SELECT * FROM passcode.entries WHERE website = '{search}'"
        cursor.execute(select_query)
        records = cursor.fetchall()
        if len(records) >= 1:
            del_query = f"DELETE FROM passcode.entries WHERE website = '{search}'"
            cursor.execute(del_query)
            db.commit()
        else:
            return 0
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.close()


def list_entry():
    db = connect()
    cursor = db.cursor()
    # Get list of entries from database
    try:
        select_query = f"SELECT website FROM passcode.entries ORDER BY website"
        cursor.execute(select_query)
        record = cursor.fetchall()
        return record
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.close()


def repeated_site(entry):
    db = connect()
    cursor = db.cursor()
    # Check that website is not repeated
    try:
        select_query = f"SELECT website FROM passcode.entries WHERE website = '{entry}'"
        cursor.execute(select_query)
        record = cursor.fetchall()
        if len(record) > 0:
            return True
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.close()


def repeated_pass(entry):
    db = connect()
    cursor = db.cursor()
    # Check that password is not repeated
    try:
        select_query = f'SELECT password FROM passcode.entries'
        cursor.execute(select_query)
        record = cursor.fetchall()
        for i in record:
            if decrypt(get_key('secret_key', 'secret'), i[0]) == entry:
                return True
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.close()
