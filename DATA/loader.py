from DATA import module

def load_data(conn):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT title, description, priority, deadline, status
        FROM Tasks
    """)

    rows = cursor.fetchall()

    results = []
    for row in rows:
        task_tuple = (
            row["title"],
            row["description"],
            row["priority"],
            row["status"],
            row["deadline"]
        )

        results.append(module.Task.from_tuple(task_tuple))

    return results
