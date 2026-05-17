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

