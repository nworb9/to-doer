import sqlite3


DB_PATH = 'db/todo.db'
NOT_STARTED = 'Not Started'
IN_PROGRESS = 'In Progress'
COMPLETED = 'Completed'


def init_table():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    query = open('./sql/create_items.sql', 'r').read()
    c.execute(query)
    conn.commit()
    c.close()
    conn.close()
    print("Table initialized!")


def add_to_list(item):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('insert into items(item, status) values(?,?)', (item, NOT_STARTED))
        conn.commit()
        c.close()
        conn.close()
        return {"item": item, "status": NOT_STARTED}
    except Exception as e:
        print('Error :: ', e)
        return None
