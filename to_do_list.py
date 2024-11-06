tasks = []
check_mark = "\u2713"  # ✓
cross_mark = "\u2717"  # ✗

def add_tasks():
    task_name = input("Enter the task: ")
    tasks.append({"name":task_name, "completed":False})
    print(f"Task '{task_name}' added successfully!")


def view_tasks():
  if not tasks:
     print("No tasks found")
  else:
     print("\n To-Do-List:")
     for idx, task in enumerate(tasks, start=1):
        status = check_mark if task["completed"] else cross_mark
        print(f"{idx}.{task['name']}-[{status}]")


def mark_task_complete():
   view_tasks()
   try:
      task_num = int(input("Enter the task number to mark it as complete: "))
      if 0<=task_num < len(tasks):
         tasks[task_num]["completed"]=True
         print(f"Task '{tasks[task_num]['name']}'marked as complete!")
      else:
         print("Invalid task number")
         
   except ValueError:
      print("Please enter a valid number")




def delete_tasks():
   view_tasks()
   try:
      task_num = int(input("Enter the task number to delete: "))
      if 0<=task_num < len(tasks):
         removed_tasks = tasks.pop(task_num)
         print(f"Task '{tasks[task_num]['name']}' deleted successfully!")
      else:
         print("Invalid task number")

   except ValueError:
      print("Please enter valid number")


def main():
   print("Welcome to TO-Do-List App")
   while True:
      print("\n Menu: ")
      print("1.Add tasks")
      print("2.View tasks")
      print("3.Mark tasks as complete")
      print("4.Delete tasks")
      print("5.Exit")

      choice = input("Choose an option(1-5):")

      if choice == "1":
         add_tasks()
      elif choice == "2":
         view_tasks()
      elif choice == "3":
         mark_task_complete()
      elif choice == "4":
         delete_tasks()
      elif choice == "5":
         print("Exiting the To-Do-List App")
         break
      else:
         print("Invalid choice. Please try again.")


if __name__ == '__main__':
   main()



