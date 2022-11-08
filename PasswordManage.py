import os, ast
data = dict()

#menu
def Menu():
    os.system("cls")
    print("Account, Pssword mannagement System")
    print("------------------------------------------------------------")
    print("1. Add Account, Pssword")
    print("2. Display Account, Pssword")
    print("3. Modify Account, Pssword")
    print("4. Delete Account, Pssword")
    print("0. End program")
    print("------------------------------------------------------------")
    

#read data from the file
def ReadData():
    with open('password.txt', 'r', encoding=('UTF-8-sig')) as f:
        filedata = f.read()
        if filedata != "":
            data = ast.literal_eval(filedata)
            return data
        else:
            return dict()

def AddData():
    while True:
        name = input("Enter an account: ")
        if name == "":
            break
        if name in data:
            print("%s is already exist" % name)
            continue
        password = input("Enter a password: ")
        data[name] = password
        with open('password.txt', 'w') as f:
            f.write(str(data))
            print("{} was completely storaged" .format(name))
            break

def DisplayData():
    print("Account \t Password")
    print("===========================================================")
    for key in data:
        print("{}\t{}" .format(key, data[key]))
    input("Press enter to return Menu")
    
    
def ModifyData():
    while True:
        name = input("Enter the account that you want to edit: ")
        if name == "":
            break
        if not name in data:
            print("%s isn't exist" % name)
            continue
        print("The original account is : %s" % data[name])
        password = input("Enter a new password: ")
        data[name] = password
        with open('password.txt', 'w', encoding=('UTF-8-sig')) as f:
            f.write(str(data))
        print("Password was completely modified")

def DelData():
    while True:
        name = input("Enter the acount that you want to delete: ")
        if name == "":
            break
        if not name in data:
            print("%s isn't exist" % name)
            continue
        print("Ｙou want to delete {}:" .format(name))
        yn = input("Y or N ?")
        if (yn == "Y" or yn == "y"):
            del data[name]
            with open('password.txt', 'w', encoding=('UTF-8-sig')) as f:
                f.write(str(data))
                input("The account had been completely deleted, you may press enter back to Menu")
                break

data = ReadData()
while True:
    Menu()
    choice = int(input("What you want(enter num): "))
    print()
    if choice == 1:
        AddData()
    elif choice == 2:
        DisplayData()
    elif choice == 3:
        ModifyData()
    elif choice == 4:
        DelData()
    else:
        break
print("program success")
