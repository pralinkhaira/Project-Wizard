# To-Do List Application

# Initialize an empty to-do list
to_do_list = []

# Function to add a task to the list
def add_task(task):
    to_do_list.append(task)

# Function to view tasks in the list
def view_tasks():
    if not to_do_list:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for idx, task in enumerate(to_do_list, 1):
            print(f"{idx}. {task}")

# Main function
def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter a task: ")
            add_task(task)
            print(f"Task '{task}' added to the to-do list.")
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
