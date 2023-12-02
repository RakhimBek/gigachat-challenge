import sqlite3

from settings import DATABASE_PATH


def fetch_all_facts():
    connection = sqlite3.connect(DATABASE_PATH)
    try:
        cursor = connection.cursor()
        cursor.execute('''select USERNAME, TEXT, FACT from FACTS''')

        return cursor.fetchall()

    except Exception as e:
        print(e)
    finally:
        connection.close()


def insert_fact(username, text, fact):
    connection = sqlite3.connect(DATABASE_PATH)
    try:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO FACTS( USERNAME, TEXT, FACT) VALUES (?, ?, ?)', (username, text, fact))
        connection.commit()

    except Exception as e:
        print(e)
    finally:
        connection.close()
