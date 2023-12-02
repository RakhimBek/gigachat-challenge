import sqlite3

from settings import DATABASE_PATH


def init_database():
    connection = sqlite3.connect(DATABASE_PATH)
    try:
        cursor = connection.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS FACTS (
            USERNAME TEXT,
            TEXT TEXT,
            FACT TEXT
        )
        ''')

        cursor.execute('CREATE INDEX IF NOT EXISTS IDX_USERNAME ON FACTS (USERNAME)')
        cursor.execute('CREATE INDEX IF NOT EXISTS IDX_TEXT ON FACTS (TEXT)')
        cursor.execute('CREATE INDEX IF NOT EXISTS IDX_FACT ON FACTS (FACT)')

        connection.commit()
        connection.close()
    except Exception as e:
        print(e)
    finally:
        connection.close()
