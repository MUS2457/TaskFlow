from datetime import datetime
from OPERATIONS import add_task, helper

def update_query(conn, colum, new_task, task_id ):  # after writing this query many times , i deside to make a fc to
    now = datetime.now()                                 # remove duplication

    cursor = conn.cursor()
    cursor.execute(f"UPDATE Tasks SET {colum} = ?, updated_at = ? WHERE id = ?",
                   (new_task, now , task_id)
    )
    conn.commit()


def update_tasks(conn):

    results = helper.search_by_title(conn)

    results_map = {i:f for i,f in enumerate(results, start=1)}

    for i, f in results_map.items() :
        print(f"{i}. {f}")

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

                column = "title"  # keep database safe by not giving user control over column and table name
                update_query(conn, column, title , task[5])
                print("Title updated")
                return

            elif choice_2 == 2:
                description = add_task.get_task_description()
                column = "description"
                update_query(conn, column, description , task[5])
                print("Description updated")
                return

            elif choice_2 == 3:
                priority = add_task.get_priority_level()
                column = "priority"
                update_query(conn, column, priority, task[5])
                print("Priority level updated")
                return

            elif choice_2 == 4:
                status = add_task.get_status()
                column = "status"
                update_query(conn, column, status, task[5])
                print("Status updated")
                return

            elif choice_2 == 5:
                deadline = add_task.get_date(task[0])
                column = "deadline"
                update_query(conn, column, deadline, task[5])
                print("Deadline updated")
                return

            print("Invalid choice")





