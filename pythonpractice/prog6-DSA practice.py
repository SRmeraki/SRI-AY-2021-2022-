
########################## GCD OPTIMIZATION #############################
# def gcd_calc(m,n):              ########### THIS IS A LONGER METHOD ##################
#     list1=[]
#     if n%m==0:
#         return m
#     elif m%n==0:
#         return n
#
#     else:
#         maximum=max(m,n)
#         for i in range(1,maximum,1):
#             if maximum%i==0:
#                 list1.append(i)
#
#         maxim = list1[0]
#
#         for j in range(1,len(list1),1):
#
#             if maximum==m and n%list1[j]==0 and list1[j]>maxim:
#                 maxim=list1[j]
#
#             elif maximum==n and m%list1[j]==0 and list1[j]>maxim:
#                 maxim=list1[j]
#
#         return maxim
#
# def gcd_method_2(m,n):                 ####### shorter and more optimized method  ########
#     maximum=max(m,n)
#     list1=[]
#     for i in range(1,maximum,1):
#         if m%i==0 and n%i==0:
#             list1.append(i)
#         list1.sort()
#
#     return list1[-1]
#
# ####### AND IF WE DONT WANT TO USE A LIST, WE CAN ALSO DO IT WITHOUT USING LISTS #####
#
# def gcd_method_3(m,n):
#     maximum = max(m, n)
#     maxim=1             ## this will store the largest common factor found so far
#     for i in range(1, maximum, 1):
#         if m % i == 0 and n % i == 0 and i>maxim:
#             maxim=i
#
#
#     return maxim
#
#  ### FOR FURTHER OPTIMIZATION, = TO SAVE TIME, WE SHOULD START SEARCHING FROM THE RIGHT END TOWARDS THE LEFT END FOR THE LARGEST NUMBER #############
#
# n=120
# m=100
#
# solution= gcd_method_3(m,n)
# print(solution)


######################################################################################

####### EUCLID'S ALGORITHM FOR GCD #############

# acc to algo = d---> divides m and n ,
#          then d---> divides m-n
#   ie ,   gcd(m,n)==gcd(n,m-n)

def gcd_euclid(m,n):

    if m<n:
        m,n=n,m   # ie technically the first number has to be the biggest

    if m%n==0:

        return (n)
    else:

        diff=m-n  # itis possible that diff >  n so for that case we need to check the condition

        return gcd_euclid(max(n,diff),min(n,diff))



m=11
n=120
solution= gcd_euclid(m,n)
print(solution)


