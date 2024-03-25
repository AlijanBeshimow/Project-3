import sqlite3


def query(sql, params=()):
    conn = sqlite3.connect('tasks.db')
    cur = conn.cursor()
    cur.execute(sql, params)
    result = cur.fetchall()
    conn.commit()
    conn.close()
    return result


query('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, title TEXT, description TEXT, category TEXT)')
