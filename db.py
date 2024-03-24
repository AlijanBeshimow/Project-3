import sqlite3


def query(sql, params=()):
    try:
        conn = sqlite3.connect('tasks.db')
        cur = conn.cursor()
        cur.execute(sql, params)
        result = cur.fetchall()
        conn.commit()
        conn.close()
        return result
    except Exception as e:
        print("Error executing query:", e)
        raise


query('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, title TEXT)')
