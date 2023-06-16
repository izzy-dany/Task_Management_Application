<img src="https://img.freepik.com/free-vector/hand-drawn-flat-design-business-communication-concept_52683-78091.jpg?t=st=1686220171~exp=1686220771~hmac=a80dd3e28989606bcd7b01a4178665b32f5ae0f47a73714dbeaaa19670c5ffa6"  width="whatever" height="whatever">


# Task Management System 📋

Task Management System is a Python program that allows users to register, add tasks, and view tasks. It incorporates polymorphism and encapsulation principles to provide flexibility and maintain data integrity.

## Features ✨

- User Registration: Users can register with a unique username and password.
- Task Addition: Users can add tasks with details such as the assigned user, title, description, and type (bug or feature).
- Task Viewing: Users can view all tasks or their own assigned tasks.

## Classes 🧬

- `User`: Represents a user with a name and a list of tasks assigned to them.

- `Task`
Represents a generic task with properties like title, description, completion status, and assignee.

- `Checklist`
Subclass of Task that specializes the task type by adding an additional property, rank, and overriding the get_details method.

- `To-do`
Subclass of Task that specializes the task type by adding an additional property, priority, and overriding the get_details method.

- `User`
Represents a user with a name and a list of tasks assigned to them. It has methods to assign tasks and display assigned tasks.

- `Project`
Represents a project with a title, description, and a list of tasks. It encapsulates the tasks within the project object, providing methods to interact with the tasks. The tasks are not directly accessible from outside the class, promoting data integrity and encapsulation.

- `TaskManager`
The TaskManager class handles user registration, task addition, and task viewing functionalities. It maintains lists of users and projects and provides methods to interact with them.


## Polymorphism 🌟

Polymorphism is demonstrated in the `assign_task` method of the `User` class. It can accept any of these task objects (`Checklist` or `To-do`) since they are subclasses of `Task`. This allows for flexibility and the ability to assign different types of tasks to users.

## Encapsulation 🔒

Encapsulation is demonstrated in the `Project` class. It encapsulates the tasks within the project object, providing methods (`add_task`, `show_progress`, `show_tasks`) to interact with the tasks. The tasks are not directly accessible from outside the class, promoting data integrity and encapsulation.

## Usage 🚀

1. Ensure you have Python installed.
2. Clone the repository: `git clone https://github.com/izzy-dany/Task_Management_Application.git`
3. Navigate to the project directory: `cd Task_Management_System`
4. Run the program: `python Task_Management_System.py`
5. Follow the on-screen instructions to register users, add tasks, and view tasks.

## LESSONS LEARNED 💡
While working on this project, several key lessons were learned:

- <b>Polymorphism</b>: Polymorphism allows for flexibility in handling different types of tasks by treating them as instances of the base Task class. It enables assigning various task types (Checklist, To-do) to users without the need for separate handling code.

- <b>Encapsulation</b>: Encapsulation promotes data integrity and better code organization. The Project class encapsulates tasks, allowing controlled access and providing dedicated methods for task addition, progress tracking, and display. It helps maintain the integrity and consistency of project data.

- <b>Inheritance</b>: Inheritance allows for creating specialized task types (Checklist, To-do) based on the generic Task class. Subclasses inherit common properties and methods from the base class while adding additional functionality specific to their task type.

- <b>Error Handling</b>: Proper error handling and input validation are crucial for maintaining program stability and preventing unexpected behaviors. Validating user input, checking for existing objects, and handling exceptions ensure smooth program execution and provide meaningful feedback to the user.

- <b>Documentation and Readability</b>: Clear documentation, meaningful variable and method names, and proper code organization greatly enhance code readability and maintainability. Adding comments, docstrings, and structuring the code into logical sections help other developers (and future self) understand the codebase more effectively.

## Contributing 🤝

Contributions are welcome! If you find any issues or want to add new features, feel free to open a pull request.

<a href="https://www.freepik.com/free-vector/hand-drawn-flat-design-business-communication-concept_20904386.htm">Image by pikisuperstar</a> on Freepik