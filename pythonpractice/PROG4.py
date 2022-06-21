# Fun Fact:- If you name a File which ends with v/ it'll create a New Folder in Pycharm!
########### FACTORIAL ###########################

# def recursive_factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * int(recursive_factorial(n-1))
#
# def iterative_factorial(n):
#     number = 1
#     for i in range(n):
#         number = number * (i+1)
#     return number
#
#
#
# n = int(input("Enter the number: "))
# print("recursive factorial is:",recursive_factorial(n))
# print("Iterative factorial is :" ,iterative_factorial(n))

###############################################################
######## FIBONACCI SERIES ###########################

# def fibo(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)
# n =int(input("enter number n "))
# print(" Nth Fibonacci Number with index starting from 0 is :",fibo(n))

################################################
#  METHOD 2
# def fibo(n):
#     a = 0
#     b = 1
#     for i in range(n):
#         print(a,end=" ")
#         a,b = b,a+b
# v = fibo(int(input("enter the number: ")))
# print(v)

########### METHOD 3 ########################

# fibo = [0,1]
# def fibonacci(n):
#     for i in range(n-2):
#         fibo.append(fibo[len(fibo) - 1] + fibo[len(fibo) - 2])
#     return fibo
# number = int(input("Enter the Number\n"))
# print("The Fibonacci series upto",number,"digits is",fibonacci(number))

###############################################################
#########  LAMBDA FUNCTIONS ##############################

# a=[[1,14],[5,6],[8,23]]
# a.sort(key= lambda x:x[1]) ##it sorts the list on the basis of
#                          ##element at index 1 ie x[1]
# print(a)

##############################################################
###   ARRAYS

# from array import *
#
# array1 = array('f',[10.2,10.1, 12, 13]) ## 'f' here is the typecast
#
# for x in array1:
#     print(x)
#
### MAPS #####

# MAPS ARE USED FOR CHANGING THE VALUES OR TYPE OR MODIFYING THE LIST

#### METHOD 1 WITHOUT USING MAPS USING FOR LOOPS
#numbers=["12","14","15","16" ]

# for items in range(len(numbers)):      ## to make changes in the elements of list, we need to use range() function
#     numbers[items] = int(numbers[items])
#
# numbers[2]= numbers[2]+2
#
# print(numbers)

#### METHOD 2 --- USING MAPS ######

# numbers=[2,3,4,5,6,7,8,9]
# square = list(map(lambda x: x*x, numbers))  ## MAP takes the function type- first and then - list on which function is to be applied
# print(square)

# Example 2
# def squ(a):
#     return a*a
# def cub(a):
#     return a*a*a
#
# func=[squ,cub]
# for i in range(5):
#     val = list(map(lambda x:x(i),func ))
#     print(val)

###### FILTERS #################

# list1=[1,2,3,45,6,7,8,9]
#
# def is_greater_5(num):
#     return num>5
#
# gr_than_5 = list(filter(is_greater_5,list1))
# print(gr_than_5)

############# REDUCE FUNCTION ################
# from functools import reduce
#
# list1= [1,2,3,4,5,6,7,8,9,10]
#
# num = reduce(lambda x,y: x+y, list1) ##reduce () sums or multiplies etc the consecutive elemets of a list or array
#
# print(num)



def performOps(A):
    m = len(A)
    n = len(A[0])
    B = []
    for i in range(len(A)):
        B.append([0] * n)
        for j in range(len(A[i])):
            B[i][n - 1 - j] = A[i][j]
    return B


A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
B = performOps(A)
for i in range(len(B)):
    for j in range(len(B[i])):
        print (B[i][j])