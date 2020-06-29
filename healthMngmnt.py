def getdate():
    import datetime
    return datetime.datetime.now()

def lock_data(n, o):
    filename = n + "_" + o + ".txt"
    with open(filename, "a") as f:
        date = str(getdate())
        f.write(date)
        f.write("\t")
        print("Enter data to lock in file : ")
        data = input()
        f.write(data)
        f.write("\n")

def retrieve_data(n, o):
    filename = n + "_" + o + ".txt"
    with open(filename, "r") as f:
        content = f.read()
        print("--- YOUR ALL DATA TILL NOW ---")
        print(content)
try:
    while(True):
        print("---- WELCOME TO THE HEALTH MANAGEMENT SYSTEM ----")
        print("Enetr 0 to exit.")
        print("Enter one of the following optons : ")
        print("1. Lock Data \n2.Retrieve Data")
        op1 = int(input())
        if op1 == 1:
            print("Enter the username from following --")
            print("Harry\nRohan\nHammad")
            print("!!! Please write in small letters only !!!")
            name = input()
            print("Enter one of the following : ")
            print("Enercise\nDiet")
            print("!!! Please write in small letters only !!!")
            option = input()
            lock_data(name, option)
        elif op1 == 2:
            print("Enter the username from following --")
            print("Harry\nRohan\nHammad")
            print("!!! Please write in small letters only !!!")
            name = input()
            print("Enter one of the following : ")
            print("Enercise\nDiet")
            print("!!! Please write in small letters only !!!")
            option = input()
            retrieve_data(name, option)
        else:
            print("Please select the correct option !!")
        if op1 == 0:
            break
except Exception as e:
    print(e)