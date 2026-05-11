class TaskAnalyser:
    def __init__(self, tasks):
        self.tasks = tasks

    def total(self):
        return len(self.tasks) if self.tasks else 0


