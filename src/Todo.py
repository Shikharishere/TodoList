from prettytable import PrettyTable, from_csv
import csv
import sys
from datetime import datetime, date
import pandas as pd


fields = [ "Task_name", "Done?", "Created At", "Completed At"]
rows = []
filename = "todo.csv"

def main():        
    # input from user
    if len(sys.argv) < 2:
        print("Welcome to Command-line Todo List")
    try: 
        if sys.argv[1] == '-h':
            print("""
            1. Use -a <taskname> for adding task.
            2. Use -d <taskname> for deleting a task.
            3. Use -c <taskname> for updating a task as completed.
            4. Use --show to see the todolist.
            5. Use -csv to create a csv file for storing user data.
            Note: Use -csv in the start. Using -csv will erase all user data. 
            """)
        elif sys.argv[1] == '-csv':
            with open(filename, 'w') as writefile:
                csvwriter = csv.writer(writefile)
                csvwriter.writerow(fields)
                print("CSV file was created")
        elif sys.argv[1] == '-a':
            created_date_time = str(date.today()) + ' ' + datetime.now().strftime("%H:%M")
            taskname = sys.argv[2]
            task = [taskname, 'No', created_date_time, '!']
            addtaskcsv(task)
        elif sys.argv[1] == '--show':
            ShowTable()
        elif sys.argv[1] == '-d':
            name = sys.argv[2]
            deletefromcsv(name)
        elif sys.argv[1] == '-c':
            taskname = sys.argv[2]
            updatecsv(taskname)

    except IndexError: 
        print("You can use -h for help\n")
        sys.exit()


# csv file
with open(filename, 'r') as readfile:
    csvreader = csv.reader(readfile)
    for row in csvreader:
        rows.append(row)

# table functions 
def ShowTable():
    try:
        with open("todo.csv") as fp:
            mytable = from_csv(fp)
        print(mytable) 

    except:
        sys.exit("Empty csv\nUse -csv to create a csv file!\n")
    else:
        if len(rows) == 1:
            print('No tasks yet')
    
    
# csv functions 
def addtaskcsv(task):
    df = pd.read_csv(filename)
    if task in df.Task_name.to_dict().values():
        sys.exit("Task already exists")
    else: 
         with open(filename, 'a') as appendfile:            
            csvappender = csv.writer(appendfile)
            csvappender.writerow(task)
            appendfile.close()
            print(f"{task[0]} was added to table.")
        
def deletefromcsv(taskname):
    if taskname == "Task_name":
        sys.exit("Invalid input")
    df = pd.read_csv(filename)
    if taskname in df.Task_name.to_dict().values():
        df = df.drop(df[df.Task_name == taskname].index)
        df.to_csv(filename, index=False)
        print(f"{taskname} was deleted!!!")
    else:
        print("Task doesn't exist")
def updatecsv(taskname):
    df = pd.read_csv(filename)
    taskname_lst = list(df.Task_name.to_dict().values())
    try: 
        num = taskname_lst.index(taskname)
    except ValueError: 
        sys.exit("Task doesn't exist!")
    df.loc[num, 'Done?'] = 'Yes ✅'
    completed_at =  str(date.today()) + ' ' + datetime.now().strftime("%H:%M")
    df.loc[num, 'Completed At'] = completed_at 
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    main()


    


