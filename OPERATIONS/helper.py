from DATA.module import Task

def search_by_title(conn):
    cursor = conn.cursor()

    while True:
        search = input("Please enter the task title of what you want to update or 'exit' to quit: ").strip()

        if search.lower() == "exit":
            print("Returning to main menu")
            break

        cursor.execute(
            "SELECT title, description, "
            "priority, deadline, status, id, "
            "created_at "
            "FROM Tasks WHERE title = ?",
            (search.upper(),)
        )

        rows = cursor.fetchall()

        if not rows:
            print("No tasks found")
            continue

        results = []

        for row in rows:
            task_tuple = (
                row["title"],
                row["description"],
                row["priority"],
                row["status"],
                row["deadline"],
                row["id"],
                row["created_at"]
            )

            results.append(task_tuple)

        return results


def print_results(rows):
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

