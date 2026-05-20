from DATA.database import create_connection, create_table, insert_into_table
from DATA.loader import load_data
from LOGIC.analyser import TaskAnalyser
from OPERATIONS import add_task, update_task, delete_task
from DATA import summary_json
from UTILS import tools

def analyse_tasks(tasks):
    if not tasks:
        print("Load tasks first.")
        return

    analyser = TaskAnalyser(tasks)
    summary = analyser.tasks_summary()
    summary_json.save_json(summary)
    print("Summary saved.")

    while True:
        print("\n=== Analysis Options ===")
        print("1. Total tasks")
        print("2. Count by status")
        print("3. Count by priority")
        print("4. Count by deadline")
        print("5. Overdue tasks")
        print("6. Due today")
        print("7. Future tasks")
        print("8. Completed tasks")
        print("9. Group by priority")
        print("10. Group by status")
        print("11. Sort by priority")
        print("12. Sort by status")
        print("13. Search inside descriptions")
        print("14. Back to main menu")

        a = input("Choose an analysis: ").strip()

        if a == "1":
            print("Total tasks:", analyser.total())

        elif a == "2":
            print("Status counts:", analyser.count_status())

        elif a == "3":
            print("Priority counts:", analyser.count_priority())

        elif a == "4":
            print("Deadline counts:", analyser.count_deadline())

        elif a == "5":
            print("\nOverdue tasks:")
            for t in analyser.overdue_tasks():
                print(t)

        elif a == "6":
            print("\nDue today:")
            for t in analyser.due_today():
                print(t)

        elif a == "7":
            print("\nFuture tasks:")
            for t in analyser.future_tasks():
                print(t)

        elif a == "8":
            print("\nCompleted tasks:")
            for t in analyser.completed_tasks():
                print(t)

        elif a == "9":
            print("\nGrouped by priority:")
            for p, group in analyser.group_by_priority().items():
                print(f"Priority {p}:")
                for t in group:
                    print("  ", t)

        elif a == "10":
            print("\nGrouped by status:")
            for s, group in analyser.group_by_status().items():
                print(f"Status {s}:")
                for t in group:
                    print("  ", t)

        elif a == "11":
            print("\nSorted by priority:")
            for t in analyser.sort_by_priority():
                print(t)

        elif a == "12":
            print("\nSorted by status:")
            for t in analyser.sort_by_status():
                print(t)

        elif a == "13":
            keyword = input("Enter keyword to search in descriptions: ")
            results = analyser.search_task(keyword)

            if not results:
                print("No results found.")
                return

            print(f"\nFound {len(results)} results:")
            for t in results:
                print(t)

        elif a == "14":
            break

        else:
            print("Invalid choice.")


def main():
    conn = create_connection()
    create_table(conn)

    tasks = None

    while True:
        print("\n=== TaskFlow Main Menu By (RaijinCode)===")
        print("1. Add new tasks")
        print("2. Load tasks from database")
        print("3. Analyse tasks")
        print("4. Update a task")
        print("5. Delete a task")
        print("6. Search tasks")
        print("7. Review summaries")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()


        if choice == "1":
            collected = add_task.get_task()

            if not collected:
                print("No tasks collected.")
                continue

            insert_into_table(conn, collected)
            print("Tasks added successfully.")


        elif choice == "2":
            tasks = load_data(conn)

            if not tasks:
                print("No tasks found in database.")
            else:
                print(f"{len(tasks)} tasks loaded successfully.")


        elif choice == "3":
            analyse_tasks(tasks)

        elif choice == "4":
            update_tasks.update_tasks(conn)


        elif choice == "5":
            delete_task.delete_task(conn)

        elif choice == "6":
            print("\nSearch Options:")
            print("1. Search by title")
            print("2. Search by status")
            print("3. Search by priority")
            print("4. Search by deadline")
            print("5. Show updated tasks only")
            print("6. Back to main menu")

            s = input("Enter your choice: ").strip()

            if s == "1":
                tools.search_title(conn)
            elif s == "2":
                tools.search_by_status(conn)
            elif s == "3":
                tools.search_by_priority(conn)
            elif s == "4":
                tools.search_by_deadline(conn)
            elif s == "5":
                tools.show_updated_tasks_only(conn)
            else:
                print("Returning to main menu.")


        elif choice == "7":
            print("\n1. Review all summaries")
            print("2. Review summary by date")
            print("3. Back")

            r = input("Enter your choice: ").strip()

            if r == "1":
                tools.review_summary()
            elif r == "2":
                tools.review_summary_by_date()
            else:
                print("Returning to main menu.")

        elif choice == "8":
            print("Goodbye.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()