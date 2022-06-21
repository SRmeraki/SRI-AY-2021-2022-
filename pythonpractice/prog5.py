# class Student:
#     no_of_stu= 10   ## the class variable can only be changed by class "Student"
#     def print_detail(self):
#         print("out of total no. of students ie",(self.no_of_stu),",", self.name," has rollno. as {0}, studies in standard {1} and has scored {2}".format(self.rollno,self.std,self.marks))
#
# harry= Student()
# rohan = Student()
# harry.name= "Harry"
# harry.rollno=23
# harry.std=12
# harry.marks= 89
#
# rohan.rollno=24
# rohan.std=12
# rohan.marks=90

# print(harry.print_detail())

######## CONSTRUCTORS ==  __init__  ##################

# class Student:
#     no_of_stu = 34   ## instance variable of the class
#     def __init__(self,arollno, standard, subject, marks):
#         self.rollno = arollno ## here rollno = INSTANCE VARIABLE and 'arollno' = argument for constructor
#                               ##we use constructor(ie, = __init__() function) so that we can define our instance variable sinside the class itself
#         self.std = standard
#         self.sub = subject
#         self.mar = marks
#
#
#     def print_detail(self):
#         print("out of total no. of students, Harry's details:"," rollno. as {0}, studies in standard {1} and has scored {2} in {3}".format(self.rollno,self.std,self.mar,self.sub))
#     ## CLASS METHODS
#     ############# CLASS METHOD  ##################
#     # IT IS A FUNCTION WHICH WILL BE ABLE TO ACCESS ONLY "INSTANCE VARIABLE OF THE CLASS"
#     ## this class method is also used when we dont want to take "SELF" as an input argument like for other functions in the class
#
#     @classmethod
#
#     def change_no_of_students(cls, new_number_of_stu):  ##here cls = class and it takes class as argument that can change the class variable "no_of_students"
#         cls.no_of_stu = new_number_of_stu
#
# #### to use CLASS METHOD as a Constructor
#     @classmethod
#     def new_string(cls,string):
#         return cls(*string.split("-"))  # *string= args that we have given which can be split into different components using the SPLIT() attribute of STRINGS.
#
# ## STATIC METHOD = WHEN WE DONT WANT TO GIVE ANY "SELF" OR "CLS" ARGUMENT TO OUR FUNCTION ##
#
#     @staticmethod
#     def print_out():
#         print("the weather is good!!")
#
# harry = Student(23,12,"Maths", 90)
# rohan = Student(24,12,"Maths",92)
# ram = Student.new_string("25-12-Maths-91")
# harry.print_detail()
# print(harry.rollno)
# print(harry.__dict__)
#
# harry.change_no_of_students(54)     ## this value of "no_of_students" will change because we are using the classmethod here
# print(harry.no_of_stu)
#
# print(rohan.no_of_stu)
# print(harry.__dict__)
#
# print(ram.rollno)
#
# ram.print_out()  ## we can use this static method with with instances like rohan,ram, harry and also with the class ie, Student. the static class will give same result for each
#
#

#################################################################################
##################################################################################
##   ABSTRACTION  AND ENCAPSULATION ##

# ABSRACTION = means to divide the function or a work in subparts or to divide a work in different classes
# ENCAPSULATION = means to hide the details of the actual working of our function from the user / hide the details of implementation

##Inheritance == to copy the class and add more functions to it
# ** it doesnt mean that we can copy paste because then it would end the concept of code reuse-ability

# SINGLE INHERIT = means single class inherits from single class

# class Programmer(Student):
#     def __init__(self,arollno, standard, subject, marks,language):
#         self.rollno = arollno ## here rollno = INSTANCE VARIABLE and 'arollno' = argument for constructor
#                               ##we use constructor(ie, = __init__() function) so that we can define our instance variable sinside the class itself
#         self.std = standard
#         self.sub = subject
#         self.mar = marks
#         self.lang = language   ## this is a new constructor of inherited class
#
#
#     def print_details(self):
#         print("out of total no. of students, Raj's details:",
#               " rollno. as {0}, studies in standard {1} and has scored {2} in {3} and uses programming language {4}".format(self.rollno, self.std,
#                                                                                           self.mar, self.sub, self.lang))
#
# raj = Programmer(24,12,"Maths",92,['Python'])
# raj.print_details()

##Multiple Inheritance= here the contructor used is the one of the 'Parent class' written first in the bracket

#and if we have same instance variable in all the 3 classes then
## the 'precedence order' of value of that variable will be == 1) its value in inherited class
#                                                       == 2) value in first written parent class

##  MULTILEVEL INHERITANCE =  it means like = 'grandson' inherits from 'son' who inherits from 'dad'
######################################################################
######################################################################

#when we override a "function" or a variable then the new function or variable is considered first and not the previous one

#ACCESS SPECIFIERS = PUBLIC = write the instance name simply
#                  = PROTECTED = write the instance name with an (_). eg: _protect
#                  = PRIVATE = write the instance name with the (__). eg : __privated

# but while printing the output with private attribute ie,
# eg: emp = Student("arguments according to the constructor ")
# so now if we want to print the private instance variable , we write
# = emp._Student__privated ==then it gives no error

################################################################
###               POLYMORPHISM   ##################3333
# WHEN A GIVEN OPERATOR PERFORMS MANY DIFFERENT FUNCTIONS , WHICH CAN BE
# DONE BY OVERRIDING: so now if we have overridden the variable and we try to print that variable then,
#  THE PRINT WILL FIRST SEARCH IN THE INSTANCE VARIABLE OF CLASS b THEN IN THE INSTANCE VARIABLE OF  CLASS a FROM WHICH b IS INHERITED

#############################   IMPORTANT  #######################
# HERE INSTANCE VARIABLE DOESNT MEAN THE ACTUAL CLASS VARIABLE -- IT MEANS THE INSTANCE VARIABLE MADE UNDER CONSTRUCTOR FUNCTION -- __INIT__

##  IF WE HAVE OVERRIDDEN THE CLASS 'a' CONSTRUCTOR IN CLASS 'b' THEN WHEN WE PRINT
#  THE INSTANCE VARIABLE THEN CLASS 'a' CONSTRUCTOR WILL NOT BE READ BECAUSE IT IS OVERRIDDEN

# BUT IF WE STILL WANT TO RUN THE CLASS 'a' CONSTRUCTOR THEN WE WILL USE
#   SUPER() METHOD IN THE __INIT__ FUNCTION OF THE INHERITED CLASS 'b'

# I.E. WE WOULD THEN WRITE "SUPER().__INIT__()" INSIDE THE __INIT__OF CLASS 'b'
# AND THE PLACE WHERE YOU HAVE WRIITEN THE SUPER () MATTERS A LOT FOR THE OUTPUT.

################################################################
################################################################
# THE METHODS LIKE __INIT__ ALL FUNCTIONS LIKE THIS ARE CALLED "DUNDER METHODS"

# SOMETIMES DDUNDER METHODS LIKE THESE CAN BE USED FOR                 "OPERATOR OVERLOADING"
# EG: INSIDE THE CLASS WE WRITE
# def __add__(self, other):
#         return self.salary + other.salary
# emp1 =Employee("Harry", 345, "Programmer")
# emp2 =Employee("Rohan", 55, "Cleaner")
# AND THEN YOU PRINT (emp1 + emp2)

# there can be many such functions which can be found in "Mapping operators as functions"

## now if we use __repr__() method == here it needs no arguments
#   eg: if we write simply
# def __repr__(self):
    # return f"Employee('{self.name}', {self.salary}, '{self.role}')"

# emp1 =Employee("Harry", 345, "Programmer")
# # emp2 =Employee("Rohan", 55, "Cleaner")
# print(emp1)    ------ then it simply goes to repr  method and prints it

# now if __str__ method is also present
# eg :def __str__(self):
#         return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"           #####      IMPORTANT      ######

# print((emp1)) //  then it will prefer to print __str__ rather than __repr__
#                 //until we dont write print(repr(emp1))

## SO THE __STR__METHOD IS TO SUMMARIZE OR DEFINE THE OBJECT THAT WE HAVE MADE

####################################################################
####################################################################
# ABSTRACT CLASS IS A CLASS THAT IS A GENERAL CLASS WHICH IS TO BE USED BY ALL OTHER CLASSES/METHODS


# it is necessary for all classes that are being derived by the abstract class to have the same method
# even though their functionality and code may differ.
#  However, the name of method should be the same as the abstract method.
#  The abstract method inside the abstract class could even be empty because we can not implement it anywhere. It is just so that all the other classes define a method by the same name.

# It is important to remember that, we can not make an object for abstract class.

# CODE:
# from abc import ABC, abstractmethod

# from abc import ABCMeta, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def printarea(self):
#         return 0
#
# class Rectangle(Shape):
#     type = "Rectangle"
#     sides = 4
#     def __init__(self):
#         self.length = 6
#         self.breadth = 7
#
#     # def printarea(self):                     //so the method taken from the abstract class must be defined separatelyin the derived class
#         return self.length * self.breadth
#
# rect1 = Rectangle()
# print(rect1.printarea())
#
###################################################################
###################################################################
# DECORATORS: Decorators are functions that take another function as an argument, and their purpose is to modify the other function without changing it.

# We can access instance attributes while using the getters and setter to validate new values. This will avoid accessing or modifying the data directly.
# By using @property, we can reuse the name of a property. This will prevent us from creating new names for the getters, setters, and deleters.

##################################################################
##################################################################
## Object Introspection

# class A:
#     Job_time = "9 to 5"
#
#     def __init__(self, name, working_days):
#         self.name = name
#         self.working_days = working_days
#
#     def introducing(self):
#         return (f"The name of the employee is:{self.name} he/she has to work for "
#                 f"{self.working_days} no. of days")
#
#     @classmethod
#     def greet(cls, time):
#         if time.upper() == "MORNING":
#             return f"Good {time}"
#         elif time.upper() == "AFTERNOON":
#             return f"Good {time}"
#         else:
#             return f"Good {time}"
#
#
# tanish = A("Tanish", 100)
# print(tanish.greet("Morning"))
# import inspect as i
#
# print(i.ismethod(tanish))
# print(i.getcomments(tanish))
# print(i.getsource(A))
# for key, data in i.getmembers(tanish):
#     if key.startswith("__"):
#         print(data)

# from array import *
# arr = array('i',[1,2,3,4,5,6,7])
# for k in (arr):    #/if i write "in range(len(arr)) then the output will show starting from index 0"
#     print(k+(k+1))
# print(type(arr))

###########################################################
###############  SPECIAL EXAMPLE   #########################
# tup1= ({'a':[1,2,3,4,5,6]},{'b':[1,2,3,4,5,6,7,8]})
# print(tup1[0]['a'])
# ##############################################################
#############################################################
#
# from functools import reduce
#
# def is_positive(num):
#     return num>0
#
#
# if __name__=='__main__':
#     num=[2,5,-7,9,4,-1,1]
#     result = list(filter(is_positive,num))  # usage of filter object
#     print(result)
#
#     extra = reduce(lambda x,y:x+y, num)
#     print(extra)

    ### IMPORTANT POINT ##:

    # IF WE WANT TO WORK WITH 'two arguments' ie, 'x and y in the same single list' so we need to use
    # "REDUCE" function rather than "filter and map".
    # and this "REDUCE function" should be imported from the library "FUNCTOOLS"


############################################################################
############################################################################

 # DECORATORS ## EXAMPLE

# def dec1(func1):
#     def nowexec():
#         print("Executing Now")
#         func1()
#         print("Executed")
#     return nowexec
# def who_is_it():
#     print("it is me ")
#
# who_is_it = dec1(who_is_it())
# who_is_it()

####################################################################################################################################

# PROPERTY , GETTER , SETTER  DECORATORS            #############################

# class Employee:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#         # self.email = f"{fname}.{lname}@codewithharry.com"
#
#     def explain(self):
#         return f"This employee is {self.fname} {self.lname}"
#
#     @property                                                         # 1  # with the use of property Decorator we can give a function as attribute with the object
#     def email(self):
#         if self.fname==None or self.lname == None:                    # 3  # ie, if somehow the email has been deleted then set it using the Setter Decorator
#             return "Email is not set. Please set it using setter"
#         return f"{self.fname}.{self.lname}@codewithharry.com"
#
#     @email.setter                                                    #2 when we want to change the variables of attribute "email" then we will use the SETTER DECORATOR
#                                                                       # first we write the attribute whose variables to change and then SETTER
#     def email(self, string):
#         print("Setting now...")
#         names = string.split("@")[0]                     # using the 0th index means the list before '@'  eg: hindustani.supporter
#         self.fname = names.split(".")[0]
#         self.lname = names.split(".")[1]
#
#     @email.deleter
#     def email(self):                                      #3 we made a 'DELETER DECORATOR' using the attribute 'EMAIL'
#         self.fname = None
#         self.lname = None
#
#
# hindustani_supporter = Employee("Hindustani", "Supporter")
# # nikhil_raj_pandey = Employee("Nikhil", "Raj")
#
# print(hindustani_supporter.email)                                  #1 # so here we have given email as attribute and not as a function and still it updates the name US
#
# hindustani_supporter.fname = "US"
#
# print(hindustani_supporter.email)
#
# hindustani_supporter.email = "this.that@codewithharry.com"        #2 # so this string is given as an input to the setter
# print(hindustani_supporter.fname)
#
# del hindustani_supporter.email                                     #3 #
# print(hindustani_supporter.email)
# hindustani_supporter.email = "Harry.Perry@codewithharry.com"
# print(hindustani_supporter.email)
#
# def solution(blocks):
#     # list1 = ['a' for 'a' in blocks]
#     blocks.split('a')
#     print(blocks)
#     # i = min(list1)
#     # print(i)
# if __name__ == '__main__':
#     blocks='abbabaaab'
#     solution(blocks)

####################################################################
############## GENERATOR OBJECTS ##################################################


# def fibo(n):                ## FIBONACCI SERIES USING GENERATOR
#     a=0
#     b=1
#     for i in range(n):
#         yield a
#         a,b = b, a+b
# g = fibo(10)
# print(g)
# print(g.__next__())    ## or [ for i in g:
#                                    # print(i) ]
# print(g.__next__())

# def fact(n):                          ##  FACTORIAL USING GENERATOR
#     last=n
#     prev=n-1
#     for i in range(n-1,0,-1):
#         m= last*prev
#         last,prev=m,prev-1
#     yield m
#
# g=fact(5)
# print(g)
# print(g.__next__())  ##  because here we have to only mention the factorial


##############################################################################################

#################### PYTHON COMPREHENSION TYPES ##############################################
###########################################################################33

# a=int(input('Enter the total no. of inputs '))
# list1 = input("Enter your items ")
# final_list= list1.split()
# while(1):
#     n= int(input(f'Choose from the options below: 1.list comprehension 2.Dictionary Comprehension 3.Set comprehension 4.Generator comprehension '))
#
#     if n==1:
#         ## list comprehension ie. []
#         out = [i for i in final_list]
#         print(f'the list comprehension is {out}')
#         continue
#
#     elif n==2:
#         ## dict comprehension ie. {} with key,value
#         diction = {i : f'item{str(i)}' for i in final_list}
#         print(f'the dictionary comprehension is {diction}')
#         continue
#
#     elif n==3:
#         ## set comprehension ie. {}
#         set_comp = {i for i in final_list}
#         print(f'the set comprehension is {set_comp}')
#         continue
#
#     elif n==4:
#         ## generator comprehension ie. ()
#         gen = (i for i in final_list)
#         print(gen.__next__())
#         print(gen.__next__())
#         print(gen.__next__())    ## this prints only till 3rd index
#         ## or
#
#         continue
#
#     else:
#         print(f'you entered wrong choice')
#         break


############################################################################

########### USING FOR LOOP WITH ELSE STATEMENT ###########################

# EG:
# for i in range(1,50):
#     if i==0:       # ie, when the 'for loop' doesn't have any break statements or when none
#                    # of the conditions in the 'for loop' are satisfied, then we can get to
#                    # ELSE STATEMENT in the FOR LOOP
#
#         break
# else:
#     print(f'Number not divisible by 2')

##########################################################################################

########################## FUNCTION CACHING #######################################

##########################################################

#  FUNCTION CACHING: we save the input and output value of a function , so that if a person runs that function later , then it can get the same desired value, ie, we will directly get the output
#                      without having to run the whole function again
# how we import LRU_CACHE FROM FUNCTOOLS MODULE
# THIS (lru_cache stores or saves the latest n values in its memory, which is given be MAXSIZE=(something)) so that a person doesnt waste memory in running the function again
# ie, when the function is called again for n values then, it will give the output directly and will not have to run again
# -------------------------------SO OVERALL IT CAN PREVENT FROM WASTING MEMORY FOR RERUNNING SIMILAR CALLS-------------------------------------------------------------------

#EG
# from functools import lru_cache
# @lru_cache(maxsize=10)
# def func1(n):
#     for i in range(n):
#         if i%2==0:
#             print(i)
#         else:
#             print('not divisible by 2')
# n=int(input('how many elementsto enter? '))
# func1(n)
# print('first option taken')
# n=int(input('how many elementsto enter? '))
#
# func1(n)
# print('2nd option taken')
#
# n=int(input('how many elementsto enter? '))
#
# func1(n)
# print('last option taken')

##############################################################################################################

# 'FINALLY' KEYWORD IS USED IN 'TRY-EXCEPT STATEMENTS' IN FILE HANDLING so that
#  all the files that we have opened during the process irrespective of any ongoing processes, or errors
# should be closed in the end , and those file closing statements can be written under the 'FINALLY' keyword

##############################################################

# and for "ELSE STATEMENTS ":  ONLY ONE THING OUT OF "except" or "else" statement will run

##############################################################

# we can print various "except statements" for exception handling of various errors like :
# 1. END OF FILE ERROR = EOFError  , 2. IOError = such file or directory doesnt exist

####################################################################
########################################################################################################
########################################################################################################

# CO-ROUTINES #

# A generator is a function that produces a sequence of results instead of returning a value.
# You generate a series of values (using the yield statement).
# Generators produce data
# Coroutines consume data
# 'Coroutines are mostly used in cases of time-consuming programs, such as tasks related to machine learning or deep learning algorithms' or in cases where the program has to read a file containing a large number of data.

# In such situations, we do not want the program to read the file or data, again and again, so we use coroutines to make the program more efficient and faster.

# Coroutines run endlessly in a program because they use a while loop with a true or 1 condition so it may run until infinite time.
# Even after yielding the value to the caller, it still awaits further instruction or calls. We have to stop the execution of coroutine by calling coroutine.close() function.
# When you call a coroutine, nothing happens.They only run in response to the next() and send() methods.Coroutine requires the use of the next statement first so it may start
# its execution.Without a next() it will not start executing.We can search a coroutine by sending it the keywords as input using object name along
# with send().The keywords to be searched are send inside the parenthesis.
# send() — used to send data to coroutine
# close() — to close the coroutine

# eg:
# def myfunc():
#     print("Code With Harry")
#     while True:                                ## this protion is used in the coroutines
#         value = (yield)                         ##      """"""
#         print(value)
#
# coroutine =myfunc()
# next(coroutine)                                  ## this "next() method" is required to start the execution of the "co-routine"
# coroutine.send("Python")
# coroutine.send(" Tutorial ")                     ## these statements will print "Python " and "Tutorial"
#
# coroutine.close()                                ## the "close() statement" is required to "stop the infinite while loop" of the co-routine.

# eg2:

# def searcher():
#     import time
#     # Some 4 seconds time consuming task
#     book = "This is a book on harry and code with harry and good"
#     time.sleep(4)
#
#     while True:
#         text = (yield)
#         if text in book:
#             print("Your text is in the book")
#         else:
#             print("Text is not in the book")
#
# search = searcher()
# print("search started")
# next(search)
# print("Next method run")
# search.send("harry")
#
#
# search.send("harry")
# input("press any key")
# search.send("harry and")
# input("press any key")
# search.send("thi si")
#
# search.close()

###############################################################################################################################
################################################################################################################################

# import os
#
# print(os.environ.get('HOME'))  ## this environment variable "HOME" is not set that is why we see its environment variable as NONE
#
# print(os.environ.get('PATH'))

#########################################################################################




