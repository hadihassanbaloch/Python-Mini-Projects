from operations import TaskStorage, Todo

def main():
    storage = TaskStorage()
    todo = Todo(storage)
    while True:
        print("1. Add Task\n 2. Read Task\n 3. Update Task\n 4. Delete Task\n 5. Exit")
        choice = input("Enter Your Choice: ")
        if choice == "1":
            title = input("Enter Title: ")
            description = input("Enter Description: ")
            todo.add_task(title, description)
        elif choice == "2":
            print(todo.read_task())
        elif choice == "3":
            title = input("Enter Title: ")
            status = input("Enter Status: ")
            todo.update_task(title, status)
        elif choice == "4":
            title = input("Enter Title: ")
            todo.delete_task(title)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Please Choose Between 1 - 5")

if __name__ == "__main__":
    main()