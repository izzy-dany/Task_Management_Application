# Task Manager 📋

Task Manager is a Python program that allows users to register, add tasks, and view tasks. It incorporates polymorphism and encapsulation principles to provide flexibility and maintain data integrity.

## Features ✨

- User Registration: Users can register with a unique username and password.
- Task Addition: Users can add tasks with details such as the assigned user, title, description, and type (bug or feature).
- Task Viewing: Users can view all tasks or their own assigned tasks.

## Classes 🧬

- `Task`: Represents a generic task with properties like title, description, completion status, and assignee.
- `Checklist` and `To-do`: Subclasses of `Task` that specialize the task types by adding additional properties (`rank` and `priority` respectively).
- `User`: Represents a user with a name and a list of tasks assigned to them.
- `Project`: Represents a project with a title, description, and a list of tasks.
- `TaskManager`: Handles user registration, task addition, and task viewing functionalities.

## Polymorphism 🌟

Polymorphism is demonstrated in the `assign_task` method of the `User` class. It can accept any of these task objects (`Checklist` or `To-do`) since they are subclasses of `Task`. This allows for flexibility and the ability to assign different types of tasks to users.

## Encapsulation 🔒

Encapsulation is demonstrated in the `Project` class. It encapsulates the tasks within the project object, providing methods (`add_task`, `show_progress`, `show_tasks`) to interact with the tasks. The tasks are not directly accessible from outside the class, promoting data integrity and encapsulation.

## Usage 🚀

1. Ensure you have Python installed.
2. Clone the repository: `git clone https://github.com/izzy-dany/Task_Management_System.git`
3. Navigate to the project directory: `cd Task_Management_System`
4. Run the program: `python Task_Management_System.py`
5. Follow the on-screen instructions to register users, add tasks, and view tasks.

## Contributing 🤝

Contributions are welcome! If you find any issues or want to add new features, feel free to open a pull request.