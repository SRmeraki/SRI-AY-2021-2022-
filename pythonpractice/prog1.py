#import flask
#a= ("hello world 6","welcome to the new world")
#print("welcome to the new world {0:e}".format(200))
#string= '2.3'
#srtinp="3"

"""print ('enter two numbers')
b= float(input())
c= float(input())
print("the sum of numbers is : ", int(b+c)) """

#string slicing
###########
#a = "hi {} i\'m swescha"
#c= print(a.format("i"))
#b= print(c.replace("i\'m","was"))
#print(a.rstrip("cha"))
#print(a.format("i"))
#print(a.join("she"))
#print(a[::-1])

#Lists (it can change)
#(mutable and same numbers can be added in the list again and again

#numbers = [2, 7, 6, 9, 11]
# slicing of lists
#print(numbers[-1:-6:-3])  # here like the string case, we have right side addresses not included
#numbers.append(7)
#numbers.pop()
#numbers.remove(9)
#print(numbers)

#TUPLE (original doesnt change)
#(immutable)


#tp = (1,2,3)

#print(tp.index(3,0,3))

##################3
#Dictionary
#d1= {"harry":"bun",
#     "swiss": "burger",
#     "avi": "milk",
    #     "swescha":{"b": "milk , bread","l": "rice, curd, veggie",
    #                "d": "roti, veggie"},
 #        "ravi":[2,3,4,5]}
 #   d1["ravi"].append("milk")
 #   print(d1["ravi"])
 #
 #   d1["will"]= ("east","west","north","south")
 #   print(d1["will"].index("west",0,4))
 #   print(d1["will"])

##########Dictionary of words################

#d1= {"apple":"its a fruit",
#     "happy":"when you smile and laugh a lot",
 #    "sad":" when you are worried",
  #   "smirk":"when you plan something cunning"}

#print("enter the word you want to search ")
#print(d1[input().lower()])

#################################
##### SET ####################
#(Set retains only the unique values)

#s= set()
#tup=("1","2","3","4")
#l1=[1,2,34,5]
#l1.append(55)
#l1.append(5)
#print(set(l1))

#s1= set()
#s1.add(12)
#s1.add(1)
#s2= s1.intersection({12,1,2,3})
#print(s2)

######## IF-ELSE-STATEMENTS ##################3

#print("enter 2 numbers: ")
#a1= int(input())
#b1= int(input())

#sum_up= a1+b1
#mul= a1* b1
#div= (a1/b1)
#remain= a1 % b1
#print("Enter your Favourite Operation: 1. Sum , 2: mul, 3: div"
#      "4: remainder")

#c1= int(input())
#if c1==1:
#    print(sum_up)

#if a1>=b1:
#    print("{0} is greater and equal to {1}".format(a1,b1))
#elif a1==b1:
#    print("is greater")
#elif c1==2:
#    print(mul)
#elif c1==3:
#    print("{0:.2f}".format(div))
#elif c1==4:
#    print(remain)
#else:
#    print("which other operation you want to perform? ")
#    s1= input()

#    print("{0} operation not available".format(s1))

#l1=[12,13,14,12,13]
#print(15 in l1)

#if 12 in l1:
#    print("yes it is")

###############################################
############ Faulty Calculator ################

#print("enter the operation to perform: 1.sum"
#      "2. mul 3. div 4.sub")
#a= int(input())
#b= int(input("enter number 1: "))
#c= int(input("enter number 2: "))

#if a==1:
#    if ((b==56) and (c==9)) or ((b==9) and (c==56)):
#        print(77)
#    else:
#        print(b+c)
#elif a==2:
#    if (b==45 and c==3) or (b==3 and c==45):
#        print(555)
#    else:
#        print(b*c)
#elif a==3:
#    if (b==56 and c==6):
#        print(4)
 #   else:
#        print(int(b/c))
#elif a==4:
#    print(b-c)
#else:
#    print("such operation not available!!")

########## FOR LOOPS ################

#tup= [["ape",1],["baby",2],["can",3],["den",4],["eel",5]]
#dict1 = dict(tup)

#for item,number in dict1.items():
#    if number <=3:
#        print(item,number)
#    else:
#        print(item,"has too much quantity")

#####  MAKE A LIST AND PRINT ONLY THOSE ITEMS WHICH ARE NUMBERS
######## AND GREATER THAN 6 #############################

#list1 = [2, "era", 3,4,5,6,7,"swescha", 12, 15 , 100]

#for item in list1 :
#    if type(item)==int and item>6:  #####str(item).isnumeric()
#          print(item)

######## WHILE LOOP##################
print("Enter Numbers: ")
while(int(input()) < 100):
    continue
print("CONGRATULATIONS!! YOU ENTERED A NUMBER GREATER THAN 100")

####### OR ###########33
#while(1):
#    a = int(input())
#    if a>100:
#        print("congratulations")
#    else:
#        continue

#######################################
#    if i==45:
#        break
#    i=i+1
#    if i>45:
#        print("hi")
#################################################################
#####3 GUESS THE NUMBER ############
print("enter your favourite number ")
i=3
while(i>0):
    a = int(input())
    if a>18:
        print("Your number is greater ""try again")
        i=i-1
        print("No.of guesses left {}".format(i))
        continue

    elif a<18:
        print("Your number is lesser ""try again")
        i=i-1
        print("No.of guesses left {}".format(i))
        continue
    elif a==18:
        print("BINGO!! You Won")
        print("you took {} guesses to win".format(4-i))
        break

print("GAME ENDED")