# Initialize an empty to-do list
to_do_list = []


# Function to add a task to the list
def add_task(task):
    to_do_list.append(task)
    print(f"Task '{task}' added to the to-do list.")


# Function to remove a task from the list
def remove_task(task):
    if task in to_do_list:
        to_do_list.remove(task)
        print(f"Task '{task}' removed from the to-do list.")
    else:
        print(f"Task '{task}' not found in the to-do list.")


# Function to display the current to-do list
def display_list():
    if len(to_do_list) > 0:
        print("To-Do List:")
        for i, task in enumerate(to_do_list, start=0):
            print(f"{i+1}. {task}")
    else:
        print("Your to-do list is empty.")


# Main loop to interact with the to-do list
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Display the to-do list")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == '3':
        display_list()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4).")
