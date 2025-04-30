import os

def load_tasks(filename="tasks.txt"):
    if not os.path.exists(filename):
        return[]
    with open(filename,"r") as file:
        tasks = file.readlines()
    return[task.strip() for task in tasks]  

def save_tasks(tasks, filename="tasks.txt"):
    with open(filename,"w") as file:
        for task in tasks:
            file.write(task + "\n")


def add_task(task,tasks):
    tasks.append(task)
    print(f"task '{task}' is added")

def view_tasks(tasks):
    if not tasks:
        print("no task found")
    else:
        print("your task")
        for idx,task in enumerate(tasks,start=1):
            print(f"{idx}.{task}")

def delete_task(index, tasks):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Task '{removed}' deleted.")
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()  # load tasks first

    while True:   # infinite loop until user chooses exit
        print("\n=== To-Do List Manager ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            task = input("Enter the new task: ")
            add_task(task, tasks)
        elif choice == "3":
            view_tasks(tasks)
            try:
                task_num = int(input("Enter task number to delete: ")) - 1
                delete_task(task_num, tasks)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "4":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose between 1-4.")

if __name__ == "__main__":
    main()            
