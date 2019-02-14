#gonna create a task list 

#task ={}
tasks = []


def view_all_tasks():
    for task in tasks:
        #print(task)
        #for key,value in task.items():
        # print out the index number of the task in user type stuff by adding 1 
        # end "=" keeps it on the same line 
        print (f"{tasks.index(task) + 1 }", end=" " )
        # now we have to step through the keys 
        for key in task.keys():
            #print(key)

            print("-" , task[key], end=" ")
            #print(key, value)
            #print(key)
            #print(value)
        print("\n")





task_del  = ""           
def del_task():
    view_all_tasks()
    task_del = int(input ("which task do you want to delete? " ))-1
    #view_all_tasks()
    #ind_del = task_del-1
    #while task_del > len(tasks):
         #print ("Please select a valid Task Number")

    if task_del > int(len(tasks)):
        print ("Please select a valid Task Number")
        view_all_tasks()

    elif task_del <= len(tasks):
         del tasks[task_del]

   
    







# create a menu
def show_menu():
    print("Press 1 to add task: ")
    print("Press 2 to delete task: ")
    print("Press 3 to view all tasks: ")
    print("Press q to quit: ")

#def nef():
    #new line 
    
def add_task():
    task_input = input("enter task ")
    task_priority= input("enter priority High Med Low : ")
    task={"title": task_input,"prior": task_priority} #combining imputs to library
     #   print(task) # get rid of this later
    tasks.append(task)# adding dict to array
     #   print (tasks)# get rid of this later









#show_menu()
user_input = ""
while  user_input != "q":
    show_menu()
    user_input = input("Enter choice: ")
    if user_input == "1":
        add_task()
        #moved the rest to function for tidyness
        #task_input = input("enter task ")
        #task_priority= input("enter priority High Med Low : ")
        #task={"title": task_input,"prior": task_priority} #combining imputs to library
        #print(task) # get rid of this later
        #tasks.append(task)# adding dict to array
        #print (tasks)# get rid of this later

    elif user_input== "2":
        del_task()
        #print("delete task")

    elif user_input=="3":
        view_all_tasks()

         #   print(tasks(task.key))

          #  for x in task.keys():
           #     print (x)

       
        #print(task(key))
        




