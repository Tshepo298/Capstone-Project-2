'''Capstone template project for FCS Task 19 Compulsory task 1.
This template provides a skeleton code to start compulsory task 1 only.
Once you have successfully implemented compulsory task 1 it will be easier to
add a code for compulsory task 2 to complete this capstone'''

#=====importing libraries===========
'''This is the section where you will import libraries'''

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''



with open('tasks.txt','r+'):
     User_name = input('User name of which the task is assigned to: ')
     Title = input('Title of the task: ')
     Date_Assigned = input('Enter the date at which the task was assigned: ')
     Date_Due = input('Date Due: ')

task_completion = input("Has the task been completed? ")
if task_completion == 'Yes':
    print("Well done")
if task_completion == 'No':
    print("Finish task before due date")



with open('user.txt','w'): #confirm that it is the correct user.
     User = input("User name: ")
     Password = input("password: ")
     if User != "admin" and Password != "adm1n":
        print("Enter a valid user name or password: ")
     if User == "admin" and Password == "adm1n":
        print("Welcome Admin")
     else:
         print("User name or password invalid")

while True:
    User = input('''Please select one of the following Options below:
r - Registering a user
a - Add task
va - View all tasks
vm - view my task
e - Exit''')

    if User == 'r':
       New_username = input('Enter new Username: ')
       New_password = input('Enter new password: ')
       Confirmation = input('Confirm password: ')
       if New_password != Confirmation:
          print("Confirmation does not match Password: ")
          if New_password == Confirmation:
            print("Registration successfull")
    


    def add_task():
     if User == 'a':
       User = True
       User_name = input("Enter Username: ")
       Title = input("Enter the title of the task: ")
       description = input("Enter the description of the task: ")
       Due_date = input("Enter the due date of the task: ")
       print(add_task())
       

    def view_all():
       count = 0
       f = open('tasks.txt','r+')#open the tasks.txt
       for lines in 'tasks.txt':
           count += 1
           temp = lines.strip()
           temp = temp.split(", ")
           print("Username : ")
           print("Description: :")
           print("Date : ")
           print("Due date: ")
           print("Complete: ")
           print("\n")
           break
       f.close()

    if User == "va":   
        menu = True
        print(view_all())
        break

    def view_mytask():
        task = 0
        user = input("Please enter the username which you want to view the task for?\n")
        f = open('tasks,txt',"r+")
        for row in f: #read each row in the file
            field = row.split(", ") #split each row with a comma
            view_more = f.readlines() #read the file contents to view more

        if field:
          num_task += 1
          print("Task number: " + str(num_task) + "\nUsername: " + field[0] + "\nDescribtion: " + field[1] +
               "\n Date: " + field[2] + "\nDue Date: " + field[
                   3] + "\n" + "Completed: " + field[4] + "\n") #display the user's tasks

    if User == "vm":
       User = True
       print(view_mytask())
       break

    elif User == "e":
         print('Goodbye!!!')
         exit()
