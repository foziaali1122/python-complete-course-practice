import os
import json

FILE_NAME = "tasks.json"

class TodoApp:
    def __init__(self):
        self.tasks = self.load_tasks()

    #load tasks
    def load_tasks(self):

        if not os.path.exists(FILE_NAME):
            return []
        
        try:
            with open(FILE_NAME, "r") as file:
                content = file.read().strip()

                if not content:
                    return []
                
                return json.loads(content)
            
        except json.JSONDecodeError:
            return []
        
    #Save tasks
    def save_tasks(self):

        with open(FILE_NAME, "w") as file:
            json.dump(self.tasks, file,indent= 4)

    #Add tasks
    def add_task(self, title, priority, due_date):
        task = {
            "title": title,
            "priority": priority,
            "due_date": str(due_date),
            "completed": False
        }
        
        self.tasks.append(task)
        self.save_tasks()

    #Completed tasks
    def complete_task(self, index):

        self.tasks[index]["completed"] = True
        self.save_tasks()

    #Deleted tasks
    def delete_task(self, index):
        self.tasks.pop(index)
        self.save_tasks()

    #Edit tasks
    def edit_task(self, index,new_title):
        self.tasks[index]["title"] = new_title
        self.save_tasks()
