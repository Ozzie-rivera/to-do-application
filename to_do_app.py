task_1 = "add"
task_2 = "view"
task_3 = "delete"
task_4 = "quit application"

input_list = []

while True:
    user_input = input(f"\nWelcome, what are you looking to do today? {task_1}, {task_2}, {task_3}, or {task_4}. ")
    
    if user_input == task_1:
        task = input("\nWhat task would you like to add? ")
        input_list.append(task)
        
    
    
    elif user_input == task_2:
        if input_list:
            print("\nYour tasks are:")
            index = 1
            for task in input_list:
                print(f"{index}. {task}")
            index += 1
            
        else: 
            print("Your list is empty")
        
    
    # if delete this shows the user his list of tasks
    elif user_input == task_3:
        if input_list:
            print("\nYour task are:") 
            index = 1
            for task in input_list:
                print(f"{index}. {task}")
                index += 1
        
            try:
                user_input = input(f"\nEnter the task you would like to delete.")
                
                if user_input in input_list:
                    input_list.remove(user_input)
                    print(f"'{user_input}' has been deleted.")
                else:
                    print(f"'{user_input}' does not exist in your task list.")
            except Exception as e:
                print(f"An error occured: {e}")

    elif user_input == task_4:
        print("\nHave a good day!")
        
    else:
        print(f"\nInvalid option. please choose {task_1}, {task_2}, {task_3}, or {task_4}")
        
