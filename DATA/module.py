class Task :
    def __init__(self, title, description, priority, status, deadline):
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status
        self.deadline = deadline

    def __str__(self):
        return f'{self.title} {self.description} {self.priority} {self.status} [{self.deadline}]'

    @classmethod
    def from_tuple(cls, tuples):
        return cls(tuples[0], tuples[1], tuples[2], tuples[3], tuples[4])
