class TodoItem: 
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.title} - {status}\nDescription: {self.description}\nDue Date: {self.due_date}"
    
class TodoManager: 
    def __init__(self):
        self.todo_list = []

    def add(self, item):
        self.todo_list.append(item)
    def remove(self, item):
        self.todo_list.remove(item)
    def get_all(self): 
        return self.todo_list