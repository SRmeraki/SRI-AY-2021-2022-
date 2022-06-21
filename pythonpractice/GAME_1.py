############ SNAKE WATER GUN GAME  #############
import random

list1= ['snake', 'water', 'gun']
i=1
your_point=0
comp_point=0
while(i<=10):
    a = (random.choice(list1))

    b= str(input("Enter: s for snake, w for water, g for gun - "))

    if b.lower()=='s' and a=='water':
        print("you won!!")
        your_point=your_point+1
        i=i+1

    elif b.lower()=='w' and a=='gun':
        print("you won!!")
        your_point = your_point + 1
        i=i+1

    elif b.lower()=='g' and a=='snake':
        print("you won!!")
        your_point = your_point + 1
        i=i+1

    else:
        print("Try again!!")
        print("computer won")
        comp_point=comp_point+1
        i=i+1

print("computer points achieved = ",comp_point)
print("your points achieved = ", your_point)