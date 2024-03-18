def menu(): #this functcion prints the menu options
    print("Welcome to the To-Do List App!\n")
    print("Menu:\n1. Add a task\n2. View tasks\n3. Mark a task as complete\n4. Delete a task\n5. Quit")

def add_task(to_do, task_to_add, completion_status): #this function adds the task to the list
    to_do[task_to_add] = completion_status
    
def view_task(to_do): #this function prints the todo list
    print("\n Here is your current To-Do List\n")
    
    if (len(to_do) == 0):
        print("Your To-do is empty\n")
    
    else:    
        print(to_do, "\n")
    
def mark_complete(to_do, task_to_mark, completion_status): #this function marks the task complete
      
    to_do[task_to_mark] = completion_status
    print("\n Good Job getting it done!\n")
    

def delete_task(to_do, task_to_delete): #this function deletes the task from the list
        
    del to_do[task_to_delete]
    print("\nTask deleted\n")
    

def check_key(to_do, key): #this function checks if the task exists in the todo list
    if key in to_do: 
        return True
        
    else: 
        return False
        
def valid_input(): #this function makes sure the user enters a valid input
    while True:
        try:
            user_input = int(input("\nWhich task do you want to do? "))
            if user_input not in range(1, 6):
                raise ValueError
            return user_input
        except ValueError:
            print("Please enter a valid number between 1 and 5")
            
        finally: 
            print("----------------------------------------------")
        
to_do_list = {}
completion = ""
menu()

user_input = valid_input()
    
while (user_input != 5): #runs until the user wants to quite (5)
    if (user_input == 1): #executes the menu option 1
        
        task_to_change = input("What task would you like to add? ")
        completion = "Incomplete"
        add_task(to_do_list, task_to_change, completion)
        
        
    elif (user_input == 2): #executes the menu option 2
        
        view_task(to_do_list)
        
    elif (user_input == 3): #executes the menu option 3
        
        if (len(to_do_list) == 0):
            print("Your To-do is empty\n")
    
        else:       
            task_to_change = input("What task do want to mark as complete (Enter the task title)? ")
            task_present = check_key(to_do_list, task_to_change)
            if (task_present): #makes sure the task exists to mark complete
                completion = "Complete"
                mark_complete(to_do_list, task_to_change, completion)
            else:
                print("\nThe task you want to mark complete does not exist\n")
    
    elif (user_input == 4): #executes the menu option 4
        if (len(to_do_list) == 0):
            print("No task to delete\n")
    
        else:    
           task_to_change = input("What task do you want to delete (Enter the task title)? ")
           task_present = check_key(to_do_list, task_to_change)
           if (task_present):    #makes sure the task exist to delete
                delete_task(to_do_list, task_to_change)
           else:
               print("\nThe task you want to delete does not exist\n")
    
    
    menu()
    user_input = valid_input() #continues getting user input
    
print("Thank you for using the To-Do List App") #Thanks the user 