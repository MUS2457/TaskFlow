import re

def get_task_title():
    while True:
        title = input("Enter a Task title or 'done' to finish, 'exit' to quit: ").strip()

        if title.lower() in ("done", "exit"):
            return title.lower()

        if not title:
            print("Title cannot be empty.")
            continue

        return title.upper()


def get_task_description():
    desc = input("Enter a task description (optional): ").strip()
    return desc.capitalize() if desc else ""


def get_priority_level():
    while True:
        print("1. Low")
        print("2. Medium")
        print("3. High")
        level_map = {
            1: "Low",
            2: "Medium",
            3: "High"
        }

        value = input("Enter a priority level (1–3): ").strip()

        if value.isdigit() and int(value) in (1, 2, 3):
            return level_map[int(value)]

        print("Invalid priority. Choose 1, 2, or 3.")


def get_date(title):
    pattern = r"^\d{4}-\d{2}-\d{2}$"

    while True:
        date = input(f"Enter the deadline for '{title}' (YYYY-MM-DD): ").strip()

        if re.match(pattern, date):
            return date

        print("Invalid date format. Use YYYY-MM-DD.")

def get_status():
    while True:
        print("1. Pending")
        print("2. In progress")
        print("3. Completed")
        status_map = {
            1: "Pending",
            2: "In progress",
            3: "Completed"
        }

        status = input("Enter a status level (1-3): ").strip()

        if status.isdigit() and int(status) in (1, 2, 3):
            return status_map[int(status)]

        print("Invalid status level. Choose 1, 2, or 3.")


def get_task():
    collected = []

    while True:
        title = get_task_title()

        if title == "exit":
            print("Quitting...")
            break

        if title == "done":
            break

        description = get_task_description()
        priority = get_priority_level()
        status = get_status()
        deadline = get_date(title)

        collected.append((title, description, priority, status, deadline))

    return collected
