###### FUNCTIONS ##################

#def function1(a,b,c):
#    """THIS FUNCTION GIVES THE MEAN OF N NUMBERS""" ## THIS IS CALLED AS
                                                ##  A DOCSTRING
#    print((a+b+c)/2)

#function1(2,3,4)
#print(function1.__doc__)

######### TRY EXCEPT #######################

# if we want that due to an error in a program , the execution further
#should not stop, so we use= try- except conditions!!

#a= input("enter number1 ")
#b= input("enter number2 ")

#try:
#    print("sum of numbers is {0:.2f}".format(float(a)+float(b)))
#except Exception as e:
#    print("ERROR IN = {}".format(e))
#print("I love Python")

###################################
#FILE INPUT/OUTPUT BASICS

"""
"r" - open file for reading - default mode
"w" - open file for writing
"x" - creates a file if it doesnt exist
"a" - add more content to a file
"t" - text mode - default mode
"b" -  binary mode 
"+" - read and write
"""

#a = open("example.txt","rt")
#content = a.read()     ##if we have already read the file then afterwards
                ## 'a' pointer will be empty

#print(content)
#for line in a:     ## when you use this line
                 # then dont use the read() before
#    print(line)


# for printing separate lines we can use readline()

#print(a.readline())
#print(a.readline())

######### readlines() = creates a LIST of all the lines
#print(a.readlines())

#####3 WRITE AND APPEND #########3
#a = open("example2.txt","a")
#f= a.write("swescha will get a summer internship at a very renowned company\n"
#        "and she will succeed there\n")

#print(f)   # returns the no.of characters in the file
# a.close()
# in "w" mode we rewrite every time and remove the previous lines!1
# in add or "a" mode we append new lines to the previous
# existing lines

# READ AND WRITE MODE
a = open("example3.txt","r+")
print(a.read())
f = a.write("swescha will get a summer internship at a very renowned company\n"
        "and she will succeed there\n")

print(a.tell())     #this TELL() function shows the number or
                    # position or no. of characters that our
                    # file ptr "a" has reached to
a.seek(0)
            # seek function gets your file ptr to the position
            # which you want.eg: seek(0) brings you back to
            # beginning of file
a.close()

##### SHORTCUT TO PRINT f= open(file.txt)  and f.close() = #####
##### USING WITH BLOCK ##########################

with open("example2.txt") as f:  #with this line you dont need to write
                                 #f.close()

##################### EXERCISE ##########################
###############################################
# PATTERN PRINTING ####
def iffalsestar(n):
        while(n>0):
                print(n * "*")
                n=n-1
                continue



n= int(input("Enter a number: "))
i=0
a= int(input("Enter 1 or 0:"))


if bool(a) is True:
        while(i<=n):
                print(i * "*")
                i=i+1
                continue
                break

elif bool(a) is not True:
        iffalsestar(n)