# Date time will be used in gen_reports
user_name = ""
user_pass = ""
login = False
from datetime import datetime

def reg_user():
    # ask the user for the appropriate information

    valid_reg = False
    while valid_reg != True:
        with open("user.txt", "r+") as user_textfile:
            entered_username = input("Enter new username: ")
            entered_password = input("Enter new password: ")
            confirm_password = input("Confirm your new password: ")
            for line in user_textfile:

                # Assign the user_name and user_pass to the first split of the list and user_pass to the second split of the list

                user_name = line.split(",")[0]
                user_pass = line.split(",")[1].strip()

            # confirm if the suer enters the same password twice

                if entered_username != user_name:
                    valid_reg = True

                    break

            # GIve the user a valid response

            if valid_reg != True:

                print("\nThe username already exists!\n")

    # Confirm that the user enters the correct password

    if entered_password == confirm_password:

        # With the user text file write to the file the new username and password

        with open("user.txt", "a") as user_textfile:

            # Write in the default format back to the text file

            user_textfile.write("\n"+entered_username +
                                ", " + entered_password)

        # Tell the user that their request has been added to the user

        print("Successfully Added your username and password to the textfile")

def add_task():
    # Ask the user for the required information when adding a task

    task_username = input("Enter username of user assigned: ")
    task_title = input("Enter the title of the task: ")
    task_description = input("Enter the Description of the task: ")
    task_assigned = input("Enter todays date: ")
    task_dueDate = input("Enter the due date of the task: ")
    task_completed = "No"

    # Open the tasks.txt file as tasks_textfile

    with open("tasks.txt", "a") as tasks_textfile:

        # Write to the file by adding a line using "a" to append to the file in the preferred way or set out of the previous lines

        tasks_textfile.write(
            f"\n{task_username}, {task_title}, {task_description}, {task_assigned}, {task_dueDate}, {task_completed}")

        # Let the user know the tasks were added

        print("Successfully added a task!")

        tasks_textfile.close()

def view_all():
    with open("tasks.txt", "r+") as tasks_textfile:
        for line in tasks_textfile:

            task_username = line.split(",")[0]
            task_title = line.split(",")[1].strip()
            task_description = line.split(",")[2].strip()
            task_assigned = line.split(",")[3].strip()
            task_dueDate = line.split(",")[4].strip()
            task_completed = line.split(",")[5].strip()

            # Set out the information in a preffered way so that the user can read it clearly

            print("______________________________________________________________________\n")
            print(f"Task: \t\t\t{task_title}\nAssigned to: \t\t{task_username}\nDate assigned: \t\t{task_assigned}")
            print(f"Due date: \t\t{task_dueDate}\nTask Complete: \t\t{task_completed}\nTask Description:\n {task_description}")
            print("\n_____________________________________________________________________")

        # Close the text file

        tasks_textfile.close()

def view_mine():
    # open the text file
    count_tasks = 0
    task_username_list = []
    task_title_list = []
    task_description_list = []
    task_assigned_list = []
    task_dueDate_list = []
    task_completed_list = []

    
    with open("tasks.txt", "r+") as tasks_textfile:
        for line in tasks_textfile:

            # Count the number of tasks done by the user

            count_tasks += 1

            task_username = line.split(",")[0]
            task_username_list.append(task_username)
            task_title = line.split(",")[1].strip()
            task_title_list.append(task_title)
            task_description = line.split(",")[2].strip()
            task_description_list.append(task_description)
            task_assigned = line.split(",")[3].strip()
            task_assigned_list.append(task_assigned)
            task_dueDate = line.split(",")[4].strip()
            task_dueDate_list.append(task_dueDate)
            task_completed = line.split(",")[5].strip()
            task_completed_list.append(task_completed)

            if line.split(",")[0] == login_username:
                
                # Assign the values to the points

                

                # Set out the information in a preffered way so that the user can read it clearly
                # Customized to the user

                print("______________________________________________________________________\n")
                print(f"Task {count_tasks}: \t\t{task_title}\nAssigned to: \t\t{task_username}\nDate assigned: \t\t{task_assigned}")
                print(f"Due date: \t\t{task_dueDate}\nTask Complete: \t\t{task_completed}\nTask Description:\n {task_description}")
                print("\n_____________________________________________________________________\n")

        print("'Number of Task' - Open a task you want to edit\n'-1'\t\t - back to main menu")
        int_entered = int(input("What would you like to do?: "))
        
        if int_entered == -1:
            main_menu()
        else:
            
            with open("tasks.txt", "r+") as tasks_textfile:
                for line in tasks_textfile:
                    if line.split(",")[0] == login_username:
                        
                        # Set out the information in a preffered way so that the user can read it clearly
                        # Customized to the user for the one that they have selected

                        print("______________________________________________________________________\n")
                        print(f"Task {int_entered}: \t\t{task_title_list[int_entered-1]}\nAssigned to: \t\t{task_username_list[int_entered-1]}\nDate assigned: \t\t{task_assigned_list[int_entered-1]}")
                        print(f"Due date: \t\t{task_dueDate_list[int_entered-1]}\nTask Complete: \t\t{task_completed_list[int_entered-1]}\nTask Description:\n {task_description_list[int_entered-1]}")
                        print("\n_____________________________________________________________________\n")                                
                        break
            
            # ask the user whether they would like to edit or just mark it as completed

            int_edit = int(input("Would you like to edit(1) or mark as completed(2)?: "))
                        
            if int_edit == 1:
                            
                if task_completed_list[int_entered-1] == "No":
                                
                    task_new_username = input("Enter username of user assigned: ")
                    task_new_title = input("Enter the title of the task: ")
                    task_new_description = input("Enter the Description of the task: ")
                    task_new_assigned = input("Enter todays date: ")
                    task_new_dueDate = input("Enter the due date of the task: ")
                    task_new_completed = input("Has the task been completed?(Yes/No): ")
                                
                    count_rows = 0 
                    with open("tasks.txt", "r+") as tasks_textfile:
                        lines = tasks_textfile.readlines()
                        
                        del lines[int_entered-1]
                        

                    with open("tasks.txt", "w") as tasks_textfile:   
                        for line in lines:
                            tasks_textfile.write(line)
                        
                            
                    # With these lines above and below we are deleting the line that was originally in the textfile and rewriting it to a list
                    # It is then inserted back into the text file at the end
                    

                    with open("tasks.txt", "a") as tasks_textfile:
                        tasks_textfile.write(f"\n{task_new_username}, {task_new_title}, {task_new_description}, {task_new_assigned}, {task_new_dueDate}, {task_new_completed}")
           
            elif int_edit == 2:

                # In these lines the user is editing whether the task has been completed or not
                # The user will then have the entire line re added keeping the information in the lines list

                str_entered = input("Would you like to mark the test as complete or not?(Yes/No): ")
                with open("tasks.txt", "r+") as tasks_textfile:
                    lines = tasks_textfile.readlines()

                    del lines[int_entered-1]

                with open("tasks.txt", "w") as tasks_textfile:
                    for line in lines:
                        tasks_textfile.write(line)

                    tasks_textfile.write(f"\n{task_username_list[int_entered-1]}, {task_title_list[int_entered-1]}, {task_description_list[int_entered-1]}, {task_assigned_list[int_entered-1]}, {task_dueDate_list[int_entered-1]}, {str_entered}")
                

        

        # Close the text file

        tasks_textfile.close()

def disp_stats():

    # COUNT how many tasks are currently in the tasks file
    # count how many users are currently in the user text file
    # print out formatted nicely

    count_tasks = 0
    count_users = 0

    with open("tasks.txt", "r+") as tasks_textfile:
        for line in tasks_textfile:
            count_tasks += 1

    with open("user.txt", "r+") as user_textfile:
        for line in user_textfile:
            count_users += 1

    print("______________________________________________________________________\n")
    print(f"There is a total of {count_tasks} tasks\nThere is a total of {count_users} users")
    print("\n______________________________________________________________________")

def main_menu():

    print("\nPlease Select one of the following options:")
    if login_username == "admin":
        print("r - register user")
        print("ds - display statistics")
        print("gr -generate reports")

    print("a - add task\nva - view all tasks\nvm - view my tasks\ne - exit")

    entered_char = input("Enter a character that you would like to achieve: ")

    # If the user chooses "r" then the user will be asked to enter a new username and password - confirming the password incase the user misstypes a letter
    # part of task 2 making only the admin accessible panel

    if entered_char.lower() == "r" and login_username == "admin":
        reg_user()

    # if the user selects "a"

    elif entered_char.lower() == "a":

        add_task()

    elif entered_char.lower() == "va":

        view_all()

    # start an elif if they chose "vm"

    elif entered_char.lower() == "vm":

        view_mine()

    elif entered_char.lower() == "ds":

        disp_stats()

    elif entered_char == "gr":

        gen_reports()
    # If the user enters 'e' exit

    elif entered_char == "e":
        print("Exiting")
    
    else:
        print("Nothing Entered\nExiting...")

def gen_reports():
    total_tasks = 0
    total_completed_tasks = 0
    total_incompleted_tasks = 0
    total_overdue = 0
    with open("tasks.txt", "r+") as tasks_textfile:
        for line in tasks_textfile:
            total_tasks += 1 
            task_username = line.split(",")[0]
            task_title = line.split(",")[1].strip()
            task_description = line.split(",")[2].strip()
            task_assigned = line.split(",")[3].strip()
            task_dueDate = line.split(",")[4].strip()
            task_completed = line.split(",")[5].strip()

            if task_completed == "Yes":
                total_completed_tasks += 1
            else:
                total_incompleted_tasks += 1



            dateTimeObj = datetime.now()
            timestampStr = dateTimeObj.strftime("%d-%b-%Y")
            
            
        
            task_dueDate_list = task_dueDate.split(" ")
            
            task_dueDate = (f"{task_dueDate_list[0]}-{task_dueDate_list[1]}-{task_dueDate_list[2]}")
            
            if task_completed == "No" and datetime.strptime(task_dueDate, "%d-%b-%Y") < datetime.strptime(timestampStr, "%d-%b-%Y"):
                total_overdue += 1
                
    with open("task_overview.txt", "w") as task_overview_text:
        task_overview_text.write(f"Total Number of tasks: {total_tasks}")
        task_overview_text.write(f"\nTotal Number of Completed tasks: {total_completed_tasks}")
        task_overview_text.write(f"\nTotal number of InComplete tasks: {total_incompleted_tasks}")
        task_overview_text.write(f"\nTotal number of tasks that haven't been completed and that are overdue: {total_overdue}")
        task_overview_text.write(f"\nThe Percentage of tasks that are incomplete: {round(total_incompleted_tasks/total_tasks,2)*100}%")
        task_overview_text.write(f"\nThe Percentage of tasks that are Overdue: {round(total_overdue/total_tasks,2)*100}%")
    
    count_users = 0
    
    with open("user.txt", "r+") as users_textfile:
        for line in users_textfile:
            count_users += 1

    with open("user_overview.txt", "w") as user_overview_text:
        user_overview_text.write(f"Total Number of Users: {count_users}")
        user_overview_text.write(f"\nTotal Number of tasks: {total_tasks}")
        with open("user.txt", "r+") as users_textfile:
            for line in users_textfile:
                count_user_tasks = 0
                total_user_completed_tasks = 0
                total_user_incompleted_tasks = 0
                total_user_overdue = 0
                user_username = line.split(",")[0]
            

                with open("tasks.txt", "r+") as tasks_textfile:
                    for line in tasks_textfile:
                        
                        if line.split(",")[0] == user_username:
                            count_user_tasks += 1

                            task_completed = line.split(",")[5].strip()

                            if task_completed == "Yes":
                                total_user_completed_tasks += 1
                            else:
                                total_user_incompleted_tasks += 1
                        
                        
                            task_dueDate = line.split(",")[4].strip()
                            task_dueDate_list = task_dueDate.split(" ")
                            task_dueDate = (f"{task_dueDate_list[0]}-{task_dueDate_list[1]}-{task_dueDate_list[2]}")

                            if task_completed == "No" and datetime.strptime(task_dueDate, "%d-%b-%Y") < datetime.strptime(timestampStr, "%d-%b-%Y"):
                                total_user_overdue += 1
                
            
                
          
                
                user_overview_text.write(f"\n\nUser: {user_username}")
                user_overview_text.write(f"\nTotal of users Tasks: {count_user_tasks}")
                user_overview_text.write(f"\nPercentage of total number of tasks assigned to user: {round(count_user_tasks/total_tasks,2)*100}%")
                user_overview_text.write(f"\nPercentage assigned that have been completed: {round(total_user_completed_tasks/count_user_tasks,2)*100}%")
                user_overview_text.write(f"\nThe percentage of tasks to still be completed: {round(total_user_incompleted_tasks/count_user_tasks,2)*100}%")
                user_overview_text.write(f"\nThe percentage of tasks assigned that have not been completed and are overdue: {round(total_user_overdue/count_user_tasks,2)*100}%")
                user_overview_text.write("\n==========================================================================================================")
                

    with open("user_overview.txt", "r") as user_overview:
        print("\n___________________________________________________________________________\n")
        print("\nUser Overview: \n")
        for line in user_overview:
            print(line)
        print("\n___________________________________________________________________________\n")

    with open("task_overview.txt", "r") as task_overview:
        print("\n___________________________________________________________________________\n")
        print("\nTask Overview: \n")
        for line in task_overview:
            print(line)
        print("\n___________________________________________________________________________\n")

# While the user is not logged in loop

while login != True:

    # Enter the user login and password

    login_username = input("Enter your username: ")
    login_password = input("Enter your password: ")

    # Open a text file to read/modify to check if the user exists with the same username and password

    with open("user.txt", "r+") as user_textfile:
        for line in user_textfile:

            # Assign the user_name and user_pass to the first split of the list and user_pass to the second split of the list

            user_name = line.split(",")[0]
            user_pass = line.split(",")[1].strip()

            # confirm if the suer enters the same password twice

            if (login_username == user_name) and (login_password == user_pass):
                login = True
                print("\nYou have successfully logged in!\n")
                break

            # GIve the user a valid response

        if login != True:

            print("\nThe username or password you have entered is not valid!\n")

# Declare default values for the login of the user

# Start the loop if logged in

if login == True:
    main_menu()
    

# Close the user text file

user_textfile.close()
