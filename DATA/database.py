import sqlite3

def create_connection(db_file = "TaskFlow.db"):
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row
    return conn

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Tasks (id INTEGER PRIMARY KEY,
                                                    title TEXT,
                                                    description TEXT,
                                                    priority INTEGER,
                                                    deadline TEXT,
                                                    status TEXT,
                                                    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                                                     updated_at TEXT)'''
)

    conn.commit()


def insert_into_table(conn, tasks):
    cursor = conn.cursor()

    for task in tasks:
        cursor.execute("""
            INSERT INTO Tasks (title, description, priority, deadline, status)
            VALUES (?, ?, ?, ?, ?)
        """, (task[0], task[1], task[2], task[4], task[3]))

    conn.commit()



