# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# BBurdelsky,11.13-16.21,Added code to complete assignment 5
# ------------------------------------------------------------------------ #


# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"   # An variable that represents a file
objFile = None # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
strTask = "" # A new task for the list
strPrior = "" # A new priority


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

objFile = open(strFile, "r")
for line in objFile:
    lstData = line.split(",")
    dicRow = {"task": lstData[0].strip(), "priority": lstData[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("How would you like to work with your To Do list? Here are you choices: ")
    print("======================================================================")
    print("""
    1) Show current data
    2) Add a new item
    3) Remove an existing item
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    # File to List
    if (strChoice.strip() == '1'):
        objFile = open(strFile, "r")
        print("Formatted data:")
        for row in objFile:
            t, p = row.split(",")
            dicRow = {"task": t.strip(), "priority": p.strip()} # removes \n
            # lstTable.append(dicRow)
            print("\t" + dicRow["task"] + ", " + dicRow["priority"].strip())
        # print("Raw data:")
        # print(lstTable)
        print()  # adding a new line for presentation
        objFile.close()
        continue


    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        print("Let's add a task to your list.\n")
        strTask = str(input("\tPlease enter a task: "))
        strPrior = str(input("\tPlease enter this task's priority [High, Medium, Low]: "))
        lstTable.append({"task": strTask, "priority": strPrior})
        # loop through to print contents of list
        dicRow = {"task": strTask, "priority": strPrior}
        print("\tYour to do list now looks like this: ")
        for dicRow in lstTable:
            print("\t"*2 + dicRow["task"] + ", " + dicRow["priority"].strip())
        print()  # adding a new line for presentation
        continue

    # Step 5 - Remove a new item from the List/Table
    elif (strChoice.strip() == '3'):
        strData = str(input("Enter the complete text of the task to be removed: "))
        for dicRow in lstTable:
            if dicRow["task"].lower() == strData.lower():
                lstTable.remove(dicRow)
        print("\tThis task was removed from the To Do List\n")
        print("The remaining tasks on the list are: ")
        for dicRow in lstTable:
            print("\t" + dicRow["task"] + ", " + dicRow["priority"].strip())
        print()  # adding new line for presentation
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(strFile, "w")
        for dicRow in lstTable:
            objFile.write(dicRow["task"] + ", " + dicRow["priority"] + "\n")
        objFile.close()
        print("Your edits have been saved.")
        print("\tThe contents of the saved list are:", lstTable)
        print()  # adding a new line for presentation
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # pause to confirm exit
        print(input("You are closing the program. Press Enter to 'exit.'"))
        objFile.close()
        break  # and Exit the program
