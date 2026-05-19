from DATA.module import Task
from datetime import datetime
import re
from OPERATIONS import helper
from DATA import summary_json

def search_title(conn):
    results = helper.search_by_title(conn)
    sorted_results = sorted(results, key=lambda k: k[5])
    print("List of your results based on your title and ordered by id :")
    for result in sorted_results:
        print(f"Task id: {result[6]}")
        print(f"Task : {Task(result[0],result[1],result[2],result[3],result[4])}")
        print(f"Added time : {result[5]}")


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


        cursor.execute(
            f"SELECT title, description, priority, deadline, status, id, created_at "
            f"FROM Tasks WHERE {x} = ?",
            (status_mapper[int(user)],)
        )

        rows = cursor.fetchall()

        if not rows:
            print(f"No results found for status: {status_mapper[int(user)]}.")
            continue

        helper.print_results(rows)

def search_by_priority(conn, priority=["Low", "Medium", "High"], x="priority"):
    search_by_status(conn, priority, x)


def search_by_deadline(conn):
    cursor = conn.cursor()

    while True:
        pattern = r"^\d{4}-\d{2}-\d{2}$"

        user = input(f"Search by deadline enter a date in this format (YYYY-MM-DD) or 'exit' to quit : ").strip()

        if user == "exit":
            print("Quitting...")
            break

        elif not re.match(pattern, user) or not user :
            print("Invalid input. Please try again.")
            continue

        cursor.execute(
            "SELECT title, description, priority, status, deadline, id, created_at "
            "FROM Tasks WHERE DATE(deadline) = DATE(?) ",
            (user,)
        )

        rows = cursor.fetchall()

        if not rows:
            print(f"No results found for deadline: {user}.")
            continue

        helper.print_results(rows)


def review_summary():
    data = summary_json.load_json()

    if not data:
        print("No results found. returning back to main menu.")
        return

    for key, value in sorted(data.items()):
        print(f"Date which have been added : {key}")
        print("Task summary:")
        print(value)
        print("-" * 40)
        print()


def review_summary_by_date():
    data = summary_json.load_json()
    if not data:
        print("No results found. returning back to main menu.")
        return

    while True:
        pattern = r"^\d{4}-\d{2}-\d{2}$"
        user = input("Enter a date in this format (YYYY-MM-DD) or 'exit' to quit: ").strip()

        if user == "exit":
            print("Quitting...")
            break

        if not re.match(pattern, user):
            print("Invalid input. Please try again.")
            continue

        matches = [(x, y) for x, y in data.items() if x.startswith(user)]

        if not matches:
            print(f"No summary found for date: {user}.")
            continue

        for key, value in matches:
            print(f"Searched date : {key}")
            print(value)
            print("-" * 40)










