Task_File = "tasks.txt"
def load_tasks():
    tasks = []
    try:
        with open(Task_File, "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass
    return tasks

def save_tasks(tasks):
    with open(Task_File, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(tasks):
        task = input("Enter a new task:> ").strip()
        if task:
            tasks.append(task)
            with open(Task_File, "a") as file:
                file.write(task + "\n")
            print("Task Added...")
        else:
            print("Task cannot be empty...")

def view_tasks(tasks):
    if not tasks:
        print("Task Not Found...")
    else:
        print("\n Your Tasks...")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {tasks}")

def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            index = int(input("Enter task number to remove:> "))
            if 0 <= index < len(tasks):
                remove = tasks.pop(index)
                save_tasks(tasks)
                print(f"Removed Task:> {remove}")
            else:
                print("Invalid task number...")
        except ValueError:
            print("Please enter a valid index number...")

tasks = load_tasks()
while True:
    print("\nTo-Do List:> ")
    print("1. Add Task")
    print("2. View Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("choose an option(1/2/3/4):> ").strip()
    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        remove_task(tasks)
    elif choice == "4":
        print("Your Exiting To-Do App, \nThanks for visiting...")
        break
    else:
        print("Invalid choice. Try Again...")