from datetime import datetime

class TaskAnalyser:
    def __init__(self, tasks):
        self.tasks = tasks

    def total(self):
        return len(self.tasks) if self.tasks else 0

    def counter(self, parameter):
        results = {}

        if not self.tasks:
            return results

        for item in self.tasks:  # i create a helper fc to avoid deplicate logic
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

        for item in self.tasks:
            now = datetime.now()
            if item.deadline < now.date() and item.status != "Completed":
                results.append(item)

        return results





