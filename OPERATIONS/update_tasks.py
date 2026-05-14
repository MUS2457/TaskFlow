from datetime import datetime
from OPERATIONS import add_task

def get_results(rows) :
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

def update_tasks(conn):
    cursor = conn.cursor()
    now = datetime.now()

    while True:
        search = input("Please enter the task title of what you want to update or 'exit' to quit: ").strip()

        if search.lower() == "exit":
            print("Returning to main menu")
            break


        cursor.execute("SELECT title, description, "
                            "priority, deadline, status "
                            "FROM Tasks WHERE title = ?", (search.upper(),))

        rows = cursor.fetchall()

        if not rows:
            print("No tasks found")
            continue

        results = get_results(rows)

        results_map = {i:f for i,f in enumerate(results, start=1)}

        while True:
            select = int(input("Which task would you like to update (enter a number): ? "))

            if select not in results_map.keys():
                print("Invalid choice")
                continue

            task = results_map[select]

            while True:
                print("1. Title")
                print("2. Description")
                print("3. Priority")
                print("4. Status")
                print("5. Deadline")
                choice_2 = int(input("Please enter your choice: "))

                if choice_2 == 1:
                    title = add_task.get_task_title()

                    if title.lower() == "exit":
                        print("Returning to main menu")
                        return

                    cursor.execute("UPDATE Tasks "
                                   "SET title = ?, updated_at = ? "
                                   "WHERE id = ?", (title, now, task[5]))
                    conn.commit()
                    print("Title updated")
                    return

                elif choice_2 == 2:
                    description = add_task.get_task_description()
                    cursor.execute("UPDATE Tasks "
                                   "SET description = ? , updated_at = ? "
                                   "WHERE id = ?", (description, now ,task[5]))
                    conn.commit()
                    print("Description updated")
                    return

                elif choice_2 == 3:
                    priority = add_task.get_priority_level()
                    cursor.execute("UPDATE Tasks "
                                   "SET priority = ? , updated_at = ? "
                                   "WHERE id = ?", (priority, now, task[5]))
                    conn.commit()
                    print("Priority level updated")
                    return

                elif choice_2 == 4:
                    status = add_task.get_status()
                    cursor.execute("UPDATE Tasks "
                                   "SET status = ? , updated_at = ? "
                                   "WHERE id = ?", (status, now ,task[5]))
                    conn.commit()
                    print("Status updated")
                    return

                elif choice_2 == 5:
                    deadline = add_task.get_date(task[0])
                    cursor.execute("UPDATE Tasks "
                                   "SET deadline = ? , updated_at = ? "
                                   "WHERE id = ?", (deadline, now, task[5]))
                    conn.commit()
                    print("Deadline updated")
                    return

                print("Invalid choice")















