def load_tasks():
    '''
    loads the lists of tasks from the tasks.txt file
    :return: list of tasks
    '''
    filename=input("Enter the text filename: ")
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    '''
    saves the changes made in the list of tasks in the tasks.txt file
    :param tasks: list of tasks
    :return: updates the list of tasks
    '''
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def to_do_list():
    '''
    create/modify the list of tasks of the user
    :return: list of tasks
    '''
    global task
    tasks=load_tasks() # loads the list of tasks
    while True:
        print("Enter your choice from the menu:") # asks user for the selection of the operation
        print("1.Add a task")
        print("2.View tasks")
        print("3.Mark a task as completed")
        print("4.Exit the menu")

        choice=int(input("Enter your choice (1/2/3/4): ")) # user input for operation choice

        if choice==1: # if choice no.1, add task
            task = input("Enter task description: ") # user input for task description
            if task in tasks: # if task is already in the list
                print("The task is already added in the list.")
            else:
                tasks.append(task) # else add the task to the list
                print("Task added successfully.")
                print("Your tasks list now is:",tasks) # prints the current tasks list
                save_tasks(tasks)

            print()
        elif choice==2: # else if choice no.2, view tasks
            print("Your current task list is:")  # prints the current tasks list
            for i in tasks:
                print(i)
            print()

        elif choice==3: # else if choice no.3, mark a task completed
            task_to_mark=input("Enter the task to mark as completed.") # user input for task to be marked as completed
            if task_to_mark in tasks: # check if the task is in the list
                tasks.remove(task_to_mark) # removes the task from the to_do_list
                print("Task successfully marked as completed.")
                save_tasks(tasks)
                print()
            else:
                print("Invalid task number.Please try again.") # else if the task is not in the list
                print()

        elif choice==4: # else if choice no.4, exit the menu
            print("Successfully exited out of the menu.")
            break

        else: # else print invalid choice input
            print("Invalid choice input.Please try again (1/2/3/4).")

to_do_list()
