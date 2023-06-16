from datetime import datetime

class Task: # Represents a generic task with properties like title, description, completion status, and assignee.
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False
        self.assignee = None

    def mark_as_completed(self):
        self.completed = True

    def get_details(self):
        raise NotImplementedError("Subclasses must implement get_details method.")

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.title} ({status})"

#----------------------- Different task types --------------------------

"""
Checklist and To-do: Subclasses of Task that specialize the task types by adding additional properties (rank and priority respectively) 
and overriding the `get_details` method to include the specific details.
"""
class Checklist(Task): # type of task
    def __init__(self, title, description, rank):
        super().__init__(title, description)
        self.rank = rank

    def get_details(self):
        return f"{super().get_details()} [Rank: {self.rank}]"

class To_do(Task): # type of task 
    def __init__(self, title, description, priority):
        super().__init__(title, description)
        self.priority = priority

    def get_details(self):
        return f"{super().get_details()} [Priority: {self.priority}]"

class User: # Represents a user with a name and a list of tasks assigned to them. It has methods to assign tasks and display assigned tasks.
    def __init__(self, name):
        self.name = name
        self.tasks_assigned = []

    """
    Polymorphism is demonstrated in the assign_task method of the User class. 
    It can accept any task object (Checklist or To-do) since they are subclasses of Task. 
    This allows for flexibility and the ability to assign different types of tasks to users.
    """
    def assign_task(self, task):
        self.tasks_assigned.append(task)
        task.assignee = self
        print(f"Assigning task '{task.title}' to {self.name}")

    def show_assigned_tasks(self):
        print(f"{self.name}'s assigned tasks:")
        for task in self.tasks_assigned:
            print(task)

    def __str__(self):
        return self.name

"""
Encapsulation is demonstrated in the Project class. 
It encapsulates the tasks within the project object, providing methods (add_task, show_progress, show_tasks) to interact with the tasks. 
The tasks are not directly accessible from outside the class, promoting data integrity and encapsulation.
"""
class Project: # Represents a project with a title, description, and a list of tasks. With methods to add tasks to the project, display project progress, and show the tasks.
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_progress(self):
        completed_tasks = sum(task.completed for task in self.tasks)
        total_tasks = len(self.tasks)
        progress = (completed_tasks / total_tasks) * 100
        print(f"Project Progress: {progress}%")

    def show_tasks(self):
        print(f"{self.title} tasks:")
        for task in self.tasks:
            print(task)

    def __str__(self):
        return self.title

"""
The `TaskManager` class handles user registration, task addition, and task viewing functionalities. 
It maintains lists of users and projects and provides methods to interact with them.
"""
class TaskManager: 
    def __init__(self):
        self.users = []
        self.projects = []

    def register_user(self): # function to register a user
        print("\nCreate login details for a new user below.")
        while True:
            new_username = input("\nUsername: ")
            if self.get_user_by_username(new_username):
                print("Sorry, the username already exists. Please select another username.\n")
            else:
                break

        while True:
            new_user_password = input("Password: ")
            confirm_password = input("Confirm password: ")
            if new_user_password == confirm_password:
                break
            else:
                print("The passwords do not match. Please re-enter the password.")

        self.users.append(User(new_username))
        print("\nUser successfully registered!")

    def add_task(self):  # function to add a new task.
        print("\nEnter details about the new task below.\n")
        task_username = input("Enter the username of the person the task is assigned to: ")
        task_title = input("Title of the task: ")
        task_descr = input("Description of the assigned task: ")
        task_type = input("Type of task (Checklist/To-do): ")
        task_due_date = input("Due date (format eg. 01 Jan 2020): ")

        now = datetime.now()
        current_date = now.strftime("%d %B %Y")
        task_details = {
            "Username": task_username,
            "Task Title": task_title,
            "Description": task_descr,
            "Date Assigned": current_date,
            "Due Date": task_due_date,
            "Complete": False
        }

        with open("tasks.txt", "a") as task_file:
            task_file.write("\n" + str(task_details))

        if task_type.lower() == "checklist":
            task_severity = input("Rank task: ")
            task = Checklist(task_title, task_descr, task_severity)
        elif task_type.lower() == "to-do":
            task_priority = input("Priority of the to-do task: ")
            task = To_do(task_title, task_descr, task_priority)
        else:
            print("Invalid task type.")
            return

        user = self.get_user_by_username(task_username)
        if user:
            user.assign_task(task)
        else:
            print(f"User '{task_username}' not found.")

        project = self.get_project_by_title("Default Project")
        if project:
            project.add_task(task)
        else:
            print("Default Project not found.")

        print("\nNew task successfully added!")

    def view_all(self):
        print("\nAll tasks:")
        for project in self.projects:
            print(f"\n{project.title} tasks:")
            for task in project.tasks:
                print(task)

    def view_mine(self, username):
        user = self.get_user_by_username(username)
        if user:
            print(f"\n{username}'s assigned tasks:")
            for task in user.tasks_assigned:
                print(task)
        else:
            print(f"User '{username}' not found.")

    def mark_task_complete(self, username, task_name):
        user = self.get_user_by_username(username)
        if user:
            for task in user.tasks_assigned:
                if task.title == task_name:
                    task.mark_as_completed()
                    print(f"Task '{task_name}' marked as complete.")
                    break
            else:
                print("Task not found.")
        else:
            print(f"User '{username}' not found.")


    def get_user_by_username(self, username):
        for user in self.users:
            if user.name == username:
                return user
        return None

    def get_project_by_title(self, title):
        for project in self.projects:
            if project.title == title:
                return project
        return None

    def run(self): # function to run the main interface
        self.projects.append(Project("Default Project", "A default project"))

        while True:
            print("\n----- Task Manager -----")
            print("1. Register a new user")
            print("2. Add a new task")
            print("3. View all tasks")
            print("4. View my tasks")
            print("5. Mark as completed")
            print("0. Exit")
            choice = input("Enter your choice (0-5): ")

            if choice == "1":
                self.register_user()
            elif choice == "2":
                self.add_task()
            elif choice == "3":
                self.view_all()
            elif choice == "4":
                username = input("\nEnter your username: ")
                self.view_mine(username)
            elif choice == "5":
                username = input("\nEnter your username: ")
                task_name = input("Enter your task name: ")
                self.mark_task_complete(username, task_name)
            elif choice == "0":
                print("\nExiting the program...")
                break
            else:
                print("\nInvalid choice. Please try again.")

def main():
    task_manager = TaskManager()
    task_manager.run()

if __name__ == "__main__":
    main()