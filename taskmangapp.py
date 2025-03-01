def task():
    tasks = [] #empty list
    print("Welcome to our Task Management App")
    
    total_task = int(input("Enter the total number of tasks you want to add:"))
    for i in range(1, total_task+1):
        task_name = input(f"Enter task {i}=")
        tasks.append(task_name)
        
    print(f"Today's tasks are\n{tasks}")
    
    while True:
        operation = int(input("Enter 1-add\n2-update\n3-delete\n4-view\n5-exit"))
        if operation == 1:
            add = input("Enter the task name you want to add\n")
            tasks.append(add)
            print(f"Task {add} has been added succesfully")
        
        elif operation == 2:
            update_val = input("Enter the task name you want to update\n: ")
            if update_val in tasks:
                up = input("Enter the new task\n ")
                ind= tasks.index(update_val)
                tasks[ind] = up
                print(f"updated task {up} ")
        
        elif operation == 3:
            del_val = input("Enter the task name you want to delete\n:")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"deleted task is {del_val}\n")
                
        elif operation == 4:
            print(f"Total Tasks are {tasks}")
        
        elif operation == 5:
            print("Closing the Program")
            break
        else:
            print("Invalid Input!...Please enter the valid input: ")

task()