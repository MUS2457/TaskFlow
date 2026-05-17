from OPERATIONS import helper


def delete_task(conn):
    results = helper.search_by_title(conn)

    results_map = {i: f for i, f in enumerate(results, start=1)}

    for i, f in results_map.items():
        print(f"{i}. {f}")

    while True:
        choice = int(input("Which task would you like to delete (enter a number based on results)? "))

        if choice not in results_map :
            print("Invalid choice. Please try again.")
            continue

        task = results_map[choice]

        print(task)
        confirmation = input("Are you sure you want to delete this task ? (y) ")

        if confirmation == "y":
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Tasks WHERE id = ?", (task[5],))
            conn.commit()

            print("Deletion complete.")
            return


        print("Deletion has been cancelled.")
        break





