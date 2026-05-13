from datetime import datetime
import re

class TaskAnalyser:
    def __init__(self, tasks):
        self.tasks = tasks

    def total(self):
        return len(self.tasks) if self.tasks else 0

    def counter(self, parameter):
        results = {}

        if not self.tasks:
            return results

        for item in self.tasks:
            key = getattr(item, parameter)  # get item.status , it's good for obj , the parameter is str
            results[key] = results.get(key, 0) + 1

        return results

    def count_status(self):
        return self.counter("status")

    def count_priority(self):
        return self.counter("priority")

    def count_deadline(self):
        return self.counter("deadline")

    def overdue_tasks(self):
        results = []
        if not self.tasks:
            return results

        now = datetime.now()
        for item in self.tasks:
            if item.deadline < now.date() and item.status != "Completed":
                results.append(item)

        return results

    def due_today(self):
        results = []
        if not self.tasks:
            return results

        now = datetime.now()
        for item in self.tasks:
            if item.deadline == now.date() and item.status != "Completed":
                results.append(item)

        return results

    def future_tasks(self):
        results = []
        if not self.tasks:
            return results

        now = datetime.now()
        for item in self.tasks:
            if item.deadline > now.date() and item.status != "Completed":
                results.append(item)

        return results

    def completed_tasks(self):
        results = []
        if not self.tasks:
            return results

        for item in self.tasks:
            if item.status == "Completed":
                results.append(item)

        return results

    def group_by_priority(self):
        results = {}
        if not self.tasks:
            return results

        for item in self.tasks:
            if item.priority not in results:
                results[item.priority] = []

            results[item.priority].append(item)

        return results

    def sort_by_priority(self):
        return sorted(self.tasks, key=lambda item: item.priority, reverse=True) if self.tasks else []

    def search_task(self, keyword):
        results = []
        if not self.tasks:
            return results

        pattern = re.compile(keyword, re.IGNORECASE)
        for item in self.tasks:
            if re.search(pattern, item.description):
                results.append(item)

        return results

    def group_by_status(self):
        results = {}
        if not self.tasks:
            return results
        for item in self.tasks:
            if item.status not in results:
                results[item.status] = []
            results[item.status].append(item)

        return results

    def sort_by_status(self):
        status_order = {
            "Pending": 1,
            "In Progress": 2,
            "Completed": 3
        }

        return sorted(self.tasks, key=lambda item: status_order[item.status]) if self.tasks else []



