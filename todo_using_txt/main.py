import os 
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
TASK_FILE = "TASKS.txt"
# Create a Class
class TodoApp:
    def __init__(self, title, description, task_status:str="Pending"):
        self.title = title
        self.description = description
        self.task_status = task_status
    def create(self):
        try:
            logger.info("Creating a New task")
            with open(TASK_FILE, "a") as f:
                dt = datetime.now()
                date = dt.strftime('%Y-%m-%d')
                time = dt.strftime('%H:%M:%S')
                tasks = f"{self.title} | {date} | {time} | {self.description} | {self.task_status}\n"
                f.write(tasks)
        except Exception as e:
            raise e
        else:
            logger.info("Task created successfully")
    def read(self):
        try:
            if not os.path.exists(TASK_FILE):
                logging.error("Task file does not exist")
                return
            with open(TASK_FILE, "r") as f:
                data = f.readlines()
                for index, line in enumerate(data):
                    print(f"{index + 1} - {line}")
        except Exception as e:
            raise e
        
        else:
            logger.info("Task read successfully")
    
    def update(self):
        try:
            logger.info("Updating task")
            with open(TASK_FILE, "r") as f:
                tasks = f.readlines()
                updated_tasks = []
                found = False
                for task in tasks:
                    parts = task.strip().split("|")
                    if parts[0] == self.title:
                        parts[-1] = self.task_status
                        found = True
                    updated_tasks.append(" | ".join(parts) + "\n")
                if not found:
                    logging.error("Task not found")
                    return
            with open(TASK_FILE, "w") as f:
                f.writelines(updated_tasks)
                logger.info("Task updated Successfully")
        except Exception as e:
            raise e
    
    def delete(self):
        try:
            with open(TASK_FILE, "r") as f:
                tasks = f.readlines()             
                updated_tasks = [task for task in tasks if not task.startswith(self.title + " |")]
                if len(updated_tasks) == len(tasks):
                    logger.error("Task not found")
                    return
            with open(TASK_FILE, "w") as f:
                f.writelines(updated_tasks)
                logger.info("Task deleted Successfully")
        except Exception as e:
            raise e
    
    
def main():
    print("************ Starting TODO APP *****************\n")
    while True:
        print("""Choose what you want to do...\n
            1. Create a Task\n
            2. Read Tasks\n
            3. Update Task\n
            4. Delete Task\n
            5. Exit""")
        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Enter Task Title: ")
            description = input("Enter Task Description: ")
            task = TodoApp(title, description)
            task.create()
        elif choice == "2":
            task = TodoApp("", "")
            task.read()
        elif choice == "3":
            title = input("Enter Task Title: ")
            status = input("Enter Task Status: ")
            task = TodoApp(title, "", status)
            task.update()
        elif choice == "4":
            title = input("Enter Task Title: ")
            task = TodoApp(title, "")
            task.delete()
        elif choice == "5":
            print("Existing the todo app Goodbye!")
            break
        else:
            logger.error("Please Choose a Number Between 1-5")
            
if __name__ == "__main__":
    main()
    