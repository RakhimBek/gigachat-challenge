import sqlite3

from dtos import Fact
from settings import DATABASE_PATH


def fetch_all_facts():
    connection = sqlite3.connect(DATABASE_PATH)
    try:
        cursor = connection.cursor()
        cursor.execute('''select USERNAME, TEXT, FACT from FACTS''')

        result = cursor.fetchall()

        facts = []
        for row in result:
            facts.append(Fact(username=row[0], text=row[1], fact=row[2]))

        return facts

    except Exception as e:
        print(e)
    finally:
        connection.close()



def fetch_all_facts_of_a_user(username):
    connection = sqlite3.connect(DATABASE_PATH)
    try:
        print(username)
        cursor = connection.cursor()
        cursor.execute(f"select USERNAME, TEXT, FACT from FACTS where USERNAME like '%{username}%'")

        result = cursor.fetchall()

        facts=[]
        for row in result:
            facts.append(Fact(username=row[0], text=row[1], fact=row[2]))

        return facts

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


if __name__ == '__main__':
    fetch_all_facts_of_a_user('taechka7')
