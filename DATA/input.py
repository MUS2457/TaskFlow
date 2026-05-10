import re

def get_task_title():
    while True:
        title = input("Enter a Task title or 'done' to finish, 'exit' to quit: ").strip()

        # Handle commands
        if title.lower() in ("done", "exit"):
            return title.lower()

        # Validate title
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

        value = input("Enter a priority level (1–3): ").strip()

        if value.isdigit() and int(value) in (1, 2, 3):
            return int(value)

        print("Invalid priority. Choose 1, 2, or 3.")


def get_date(title):
    pattern = r"^\d{4}-\d{2}-\d{2}$"

    while True:
        date = input(f"Enter the deadline for '{title}' (YYYY-MM-DD): ").strip()

        if re.match(pattern, date):
            return date

        print("Invalid date format. Use YYYY-MM-DD.")


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
        deadline = get_date(title)

        collected.append((title, description, priority, deadline))

    return collected
