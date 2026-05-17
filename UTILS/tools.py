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



def search_by_status(conn, status=["Pending", "In progress", "Completed"] , x="status"):
    cursor = conn.cursor()
    status_mapper = {i: f for i, f in enumerate(status, start=1)}

    while True:
        print("\nChoose a status:")
        for key, value in status_mapper.items():
            print(f"{key}. {value}")

        user = input(f"Search by {x} (enter number) or 'exit' to quit: ").strip().lower()

        if user == "exit":
            print("Quitting...")
            break

        if not user.isdigit() or int(user) not in status_mapper:
            print("Invalid input. Please try again.")
            continue

        # run SQL
        cursor.execute(
            f"SELECT title, description, priority, deadline, status, id, created_at "
            f"FROM Tasks WHERE {x} = ?",
            (status_mapper[int(user)],)
        )

        rows = cursor.fetchall()

        if not rows:
            print(f"No results found for status: {status_mapper[int(user)]}.")
            continue

        result = []
        for row in rows:
            task_id = row["id"]
            title = row["title"]
            description = row["description"]
            priority = row["priority"]
            status = row["status"]
            deadline = row["deadline"]
            created_at = row["created_at"]

            obj = (task_id, Task(title, description, priority, status, deadline), created_at)
            result.append(obj)

        print(f"\nResults found: {len(result)}\n")
        for obj in result:
            print(f"ID        : {obj[0]}")
            print(f"Task      : {obj[1]}")
            print(f"Created at: {obj[2]}")
            print("-" * 40)
            print()

def search_by_priority(conn, priority=["Low", "Medium", "High"], x="priority"):
    search_by_status(conn, priority, x)









