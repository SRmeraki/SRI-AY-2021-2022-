######################## HEALTH MANAGEMENT SYSTEM ############
import datetime
def getdate():
    """ this function gives us a timestamp"""

    return datetime.datetime.now()

def client_name():
    """Function returns name of client"""
    a = int(input("Enter: 1 = Harry, 2 = Rohan , 3 = Simba : "))
    return a

def diet_for_client(x):
    """this function sets the diet for client"""
    if x==1:
        f = open("harry_diet.txt","wt")          ##wt is the write -text mode
        f.write(str([str(getdate())]) + ":"+ input("Enter the diet to be set "))
        f.close()

    elif x==2:
        f= open("rohan_diet.txt","wt")
        f.write(str([str(getdate())]) + ":"+ input("Enter the diet to be set "))
        f.close()

    elif x==3:
        f = open("simba_diet.txt","wt")
        f.write(str([str(getdate())]) + ":" + input("Enter the diet to be set "))
        f.close()

def exercise_for_client(x):
    """this fuction sets the exercises for clients"""
    if x == 1:
        f = open("harry_exercise.txt", "wt")
        f.write(str([str(getdate())]) + input("Enter the exercise to be set "))
        f.close()

    elif x == 2:
        f = open("rohan_exercise.txt", "wt")
        f.write(str([str(getdate())]) + input("Enter the exercise to be set "))
        f.close()

    elif x == 3:
        f = open("simba_exercise.txt", "wt")
        f.write(str([str(getdate())]) + ":" + input("Enter the exercise to be set "))
        f.close()

def retrieve_exercise(x):
    """this fuction retrieves the exercises of clients"""
    if x == 1:
        f = open("harry_exercise.txt", "rt")   ##rt is the read-text default mode
        print(f.read())
        f.close()

    elif x == 2:
        f = open("rohan_exercise.txt", "rt")
        print(f.read())
        f.close()

    elif x == 3:
        f = open("simba_exercise.txt", "rt")
        print(f.read())
        f.close()

def retrieve_diet(x):
    """this fuction retrieves the diets of clients"""
    if x == 1:
        f = open("harry_diet.txt", "rt")
        print(f.read())
        f.close()

    elif x == 2:
        f = open("rohan_diet.txt", "rt")
        print(f.read())
        f.close()

    elif x == 3:
        f = open("simba_diet.txt", "rt")
        print(f.read())
        f.close()


def main_func():

    name = client_name()
    dtime = getdate()
    option=input("Now choose whether you want to set or retrieve the data: "
          "a. Set diet "
          "b. Set Exercise "
          "c. Retrieve Diet "
          "d. Retrive Exercise ")

    if option=="a":
        diet_for_client(name)
    elif option=="b":
        exercise_for_client(name)
    elif option=="c":
        try:
            print(retrieve_diet(name))
        except Exception as e:
            print("Some Error Observed: {}".format(e))



    elif option=="d":
        try:
            print(retrieve_exercise(name))
        except Exception as e:
            print("Some Error Observed: {}".format(e))

        #retrieve_exercise(name)

print("WELCOME TO THE HEALTH MANAGEMENT SYSTEM")
print("Choose from the options below: ")

main_func()
while(1):

    inpu = input("Do you want to continue??  enter y or n ")
    if inpu=="y":
        main_func()
        continue
    elif inpu=="n":
        break

##########################################################
##########################################################

#METHOD 2

# Health Managment System
client_list = {1:"Manoj",2:"Pritesh",3:"Rushi"}
log_list = {1:"Exercise", 2:"Diet"}

def getdate():
    import datetime
    return datetime.datetime.now()

try:
    print("Select Client Name:")
    for key,value in client_list.items():
        print("Press",key,"For",value,"\n",end="")
    client_name = int(input())

    print("Press 1 for log")
    print("Press 2 for Retrieve")
    op = int(input())

    if op is 1:
        for key,value in log_list.items():
            print("Press",key,"For",value,"\n",end="")
        log_name = int(input())
        print("Selected Job:",log_list[log_name])
        f = open(client_list[client_name]+"_"+log_list[log_name]+".txt","a")
        k = 'y'
        while(k is not "n"):
            print("Enter", log_list[log_name],"\n", end="")
            mytext = input()
            f.write("["+str(getdate())+"]:"+mytext+"\n")
            k = input("Add More ? y/n:")
            continue
        f.close()
    elif op is 2:
        for key,value in log_list.items():
            print("Press",key,"to retrieve",value,"\n",end="")
        log_Name = int(input())
        print(client_list[client_name],"-",log_list[log_Name],"Report:","\n", end="")
        f = open(client_list[client_name]+"_"+log_list[log_Name]+".txt","rt")
        contents = f.readline()
        for line in contents:
            print(line,end="")
        f.close()
    else:
        print("Invalid Input !!!")
except Exception as e:
    print("Wrong Input !!!")