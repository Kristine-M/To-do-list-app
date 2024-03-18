def menu():
    print("Welcome to the To-Do List App!\n")
    print("Menu:\n1. Add a task\n2. View tasks\n3. Mark a task as complete\n4. Delete a task\n5. Quit")

def add_task(to_do, task_to_add, completion_status):
    to_do[task_to_add] = completion_status
    
def view_task(to_do):
    print("\n Here is your current To-Do List\n")
    print(to_do_list, "\n")
    
to_do_list = {}
completion = "Incomplete"
menu()
user_input = int(input("\n"))
while (user_input != 5):
    if (user_input == 1):
        new_task = input("What task would you like to add? ")
        add_task(to_do_list, new_task, completion)
        
        
    elif (user_input == 2):
        view_task(to_do_list)
        
    menu()
    user_input = int(input("\n"))
    
print("Thank you for using the To-Do List App")