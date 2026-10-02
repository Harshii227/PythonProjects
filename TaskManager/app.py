def task():
    tasks = []
    print("-----welcome to task manager app-----")
    
    total_tasks = int(input("Enter how many tasks you want to add = "))
    for i in range(total_tasks):
        task_name = input(f"Enter task {i + 1} = ")
        tasks.append(task_name)
        
    print(f"Today's tasks are\n{tasks}")
    
    while True:
        operation = int(input("Enter 1-Add\n1-Update\n2-Delete\n3-View\n4-Exit/stop/"))
        if operation == 1:
            add = input("Enter task you want to add = ")
            tasks.append(add)
            print(f"task {add} has been added successfully")
        elif operation == 2:
            updated_val = input("Enter the task you want to update = ")    
            if updated_val in tasks:
                up = input("Enter the new task = ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Updated task {up}")
            
        elif operation == 3:
            del_val = input("Which task you want to delete = ")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Task {del_val} has been deleted successfully")
                
        elif operation == 4:
            print(f"Total tasks = {tasks}") 
            
        elif operation == 5:
            print("closing the program....")  
            break         
               
        else:
            print("Invalid input")       