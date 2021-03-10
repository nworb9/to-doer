import sqlite3
from contextlib import closing


DB_PATH = 'db/todo.db'
NOT_STARTED = 'Not Started'
IN_PROGRESS = 'In Progress'
COMPLETED = 'Completed'


def init_table():
    query_sqlite(open('db/sql/create_items.sql', 'r').read())
    print("Table initialized!")


def query_sqlite(query, query_type='execute', **kwargs):
    conn = sqlite3.connect(DB_PATH)
    result = None
    with closing(conn.cursor()) as c:
        if query_type == 'execute':
            if kwargs.get('item'):
                c.execute(query, kwargs.get('item'))
            else:
                c.execute(query)
        if query_type == 'fetchall':
            c.execute(query)
            result = c.fetchall()
    conn.commit()
    return result


def add_to_list(item):
    try:
        query_sqlite('insert into items(item, status) values(?,?)', item=(item, NOT_STARTED))
        return {"item": item, "status": NOT_STARTED}
    except Exception as e:
        print('Error :: ', e)
        return None


def get_all_items():
    try:
        rows = query_sqlite('select * from items', query_type='fetchall')
        return {"count": len(rows), "items": rows }
    except Exception as e:
        print('Error :: ', e)
        return None


def get_item_status(item):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute(f"select status from items where item='{item}'")
        status = c.fetchone()[0]
        return status
    except Exception as e:
        print('Error :: ', e)
        return None


def update_status(item, status):
    if status.lower().strip() == 'not started':
        status = NOT_STARTED
    elif status.lower().strip() == 'in progress':
        status = IN_PROGRESS
    elif status.lower().strip() == 'completed':
        status = COMPLETED
    else:
        print("Invalid Status: " + status)
        return None
    try:
        query_sqlite('update items set status=? where item=?', (status, item))
        return {item: status}
    except Exception as e:
        print('Error :: ', e)
        return None

