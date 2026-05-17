from OPERATIONS import helper
from DATA.module import Task
from datetime import datetime

def search_title(conn):
    results = helper.search_by_title(conn)
    sorted_results = sorted(results, key=lambda k: k[5])
    print("List of your results based on your title and ordered by id :")
    for result in sorted_results:
        print(result)


def show_updated_tasks_only(conn):
    cursor = conn.cursor()

    cursor.execute(
        "SELECT title, description, priority, status, deadline, id, updated_at, created_at "
        "FROM Tasks WHERE updated_at IS NOT NULL"
    )

    rows = cursor.fetchall()

    if not rows:
        print("No updated tasks found, try to update a task first")
        return

    mapper = {}

    for row in rows:
        task_id = row["id"]
        title = row["title"]
        description = row["description"]
        priority = row["priority"]
        status = row["status"]
        deadline = row["deadline"]
        updated_at = row["updated_at"]
        created_at = row["created_at"]

        obj = (task_id, Task(title, description, priority, status, deadline), created_at)
        dt = datetime.strptime(updated_at, "%Y-%m-%d %H:%M:%S")

        if dt not in mapper:
            mapper[dt] = []
        mapper[dt].append(obj)

    print(f"\nResults found: {len(rows)} (updated tasks)\n")

    for key in sorted(mapper.keys(), reverse=True):
        print(f"Updated at: {key}")
        print("-" * 40)

        for task_id, task_obj, created_at in mapper[key]:
            print(f"ID        : {task_id}")
            print(f"Task      : {task_obj}")
            print(f"Created at: {created_at}")
            print("-" * 40)

        print()





