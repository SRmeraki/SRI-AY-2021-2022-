# A. Array TOPIC

# reverse a string
###############################################################
# def reverse_list(array1,l,r):
#     while(l<r):
#         array1[l], array1[r] = array1[r], array1[l]
#         l = l + 1
#         r = r - 1
#
#
#
# array1 = [int(x) for x in input().split()]## if you want to put input as string then write each letter separately with a space
# a = reverse_list(array1,0,len(array1)-1)
# print(array1)

##################################################################

# how to search the min and max with minimum number of comparisons

##################################################################

# 1.Linear Search

# class result:
#     def __init__(self):
#         self.min=0
#         self.max=0
#
# def getminmax(arr,arr_size):
#     minmax = result()    # set the first-two elements of the list as min and max accordingly and
#                         ## then test for the remaining elements from index 2 to n
#
#     if arr_size == 1:
#         minmax.min = arr[0]
#         minmax.max = arr[0]
#         return minmax
# #### if no. of elements is greater than 2
#
#     if arr[0]>arr[1]:
#         minmax.min=arr[1]
#         minmax.max=arr[0]
#     elif arr[0]<arr[1]:
#         minmax.min=arr[0]
#         minmax.max=arr[1]
#
#     for i in range(2,arr_size):
#         if arr[i] > minmax.max:
#             minmax.max = arr[i]
#         elif arr[i]< minmax.min:
#             minmax.min = arr[i]
#
#     return minmax
#
#
# ### main code ###
#
# if __name__ == "__main__":
#     arr = [105, 512, 12, 330, 3000]
#     arr_size = 5
#     minmax= getminmax(arr,arr_size)
#     print("minimum  and max number is :", minmax.min,minmax.max)

# time complexity = O(n)

# 2. Binary Search
# def getminmax(arr,start,preend):
#     minmax_min = arr[start]
#     minmax_max = arr[start]
#
#     if start==preend:  # only 1 element in the list
#         minmax_max = arr[start]
#         minmax_min = arr[start]
#         return (minmax_max, minmax_min)
#
#     elif preend==start+1:## ie, only two elements
#
#         if arr[start]>arr[preend]:
#             minmax_max=arr[start]
#             minmax_min=arr[preend]
#
#         else:
#             minmax_min= arr[start]
#             minmax_max= arr[preend]
#         return( minmax_max, minmax_min)
#
#     else: # number of n greter than 2  # BINARY SEARCH, YOU KEEP DIVIDING
#         mid = int((start + preend)/2)   ##IT IS IMP TO PUT INTEGER BOUND ON MID OTHERWISE IT WILL GO ON INFINTE RECURSIVE LOOP
#         arr_max1 , arr_min1 = getminmax(arr, start, mid)
#         arr_max2 , arr_min2 = getminmax(arr, mid+1, preend)
#
#         return(max(arr_max1 , arr_max2), min(arr_min1 , arr_min2))
#
# if __name__ == '__main__':
#     arr = [12,30,400,500,70,80]
#     low= 0
#     n = len(arr) - 1
# ans1 , ans2  = getminmax(arr,low,n)
# print("the max and min number in the array",ans1 , ans2)

## TIME COMPLEXITY : 3T(n/2) -2

# 3.Compare in Pairs
##if total number of elements are odd , and case2 when no. of elements are even

# def getminmax(arr):
#     arr_size= int(len(arr)-1)
#
#     if (arr_size)%2==0: # ie if it is an even number, then initialize the first and second number AS min and max
#         i=2
#         if arr[0]>arr[1]:
#             mx=arr[0]
#             mn=arr[1]
#
#         else:
#             mx= arr[1]
#             mn=arr[0]
#
#         while(i<arr_size):  # then check for max and min in consequtive pairs of numbers
#             if max(arr[i],arr[i+1])>mx:
#                 mx=max(arr[i],arr[i+1])
#             elif min(arr[i],arr[i+1])<mn:
#                 mn=min(arr[i],arr[i+1])
#             i=i+2  # because we are checking pairwise
#
#     else:  # ie odd number put the first number as both max and min
#         mx=arr[0]
#         mn=arr[0]
#         i=1
#         while (i < arr_size):
#             if max(arr[i], arr[i + 1]) > mx:
#                 mx = max(arr[i], arr[i + 1])
#             elif min(arr[i], arr[i + 1]) < mn:
#                 mn = min(arr[i], arr[i + 1])
#             i = i + 2
#
#     return mx, mn
#
# if __name__ == '__main__':
#     arr = [12,500,16,30,66]
#     mx, mn = getminmax(arr)
#     print(mx, mn)


## TIME COMPLEXITY = FOR ODD = 3[(N-1)/2]
                    # FOR EVEN= 1 + 3[(N-2)/2]


################################################

##############################################################

# how to get the kth smallest number

###############################################################

# 1. Using heap sort - MIN HEAP
#
# def heapify_func(arr,n,i):
#     minmum = i   # first set the root as minimum value
#     left = 2*i  # left child
#     right = (2*i)+1
#
#     if left<n and arr[left]<arr[i]: # if left child is smaller than root
#         minmum = left
#     if right<n and arr[right]<arr[minmum]: # if right child is smaller than root
#         minmum = right
#
#     # if the given root index element is not minimum, then
#     if minmum != i:
#         arr[i],arr[minmum]= arr[minmum],arr[i]
#         heapify_func(arr,n,minmum)
#
# def heapsort_func(arr, n):
#
#     ## build the min heap
#
#     for i in range(int(n/2)-1, -1 , -1): # in RANGE we can also write (starting point, ending point+1, counter (-- or ++))
#
#         heapify_func(arr,n,i)
#
#
#     ## now to remove elements from bottom of tree one by one and getting a sorted array in Descending order
#     ## ie, SWAPPING the last leaf and root and then HEAPIFY
#     for j in range((n-1), 0, -1):
#         arr[j], arr[0] = arr[0], arr[j]
#         heapify_func(arr,j,0) # first heapify the new Root and then index--
#        # j = size of heap , 0 = index at which we have to heapify
#        # as the bottom subtrees are already heapified so we just have to heapify the root indexed tree
#
#
#
# if __name__ == '__main__':
#     arr = [23, 4, 6, 9, 12, 5]
#     n = len(arr)
#     heapsort_func(arr, n)
#     k = int(input('Enter the number k: '))
#
#
#     for i in range(n):
#         print("Sorted array is : ", arr[i])
#     print("The kth smallest element is :" ,arr[n-k])


#############################################################
# SORT AN ARRAY OF ZEROES AND ONES WITHOUT USING SORTING ALGOS
##############################################################


# def sort_num(arr,n):
#     count = 0
#     count1 = 0
#     count2 = 0
#     for i in range(0,n,1):
#         if arr[i]==0:
#             count=count+1
#
#
#
#         if arr[i]==1:
#             count1=count1+1
#     print(count,count1)
#
#
#
#
#     for k in range(0,count,1):
#
#         arr[k]=0
#
#     for l in range(count,count+count1,1):
#         arr[l]=1
#
#     for m in range(count+count1,n,1):
#         arr[m]=2
#
#
# if __name__ == '__main__':
#     arr = [1,0,2,1,0,2,0,1,0,2,0]
#     n= len(arr)
#     sort_num(arr,n)
#
#     for i in range(0,n,1):
#         print(arr[i])

#############################################################################################
# SEPARATE ALL THE NEGATIVE ON ONE SIDE AND ALL THE
# POSITIVES ON THE OTHER SIDE OF THE ARRAY

###############################################################################################
#METHOD 1
# USING TWO-POINTER APPROACH ---> USING LEFT AND RIGHT VARIABLES
#
# def separate(arr,n):
#     left =0
#     right = n-1
#     while left <= right:
#
#
#         if arr[left]<0 and arr[right]<0:
#             left= left+1
#
#         elif arr[left]>0 and arr[right]>0:
#             right= right-1
#
#
#         elif arr[left]>0 and arr[right]<0:
#             arr[left],arr[right] = arr[right],arr[left]
#             left = left+1
#             right = right-1
#         else:
#             left=left+1
#             right= right-1
#
# if __name__ == '__main__':
#     arr = [12,32,44,15,-9,-32,-8,-6,5,-4]
#     n=len(arr)
#     separate(arr,n)
#     for i in range(n):
#         print(arr[i])

# METHOD 2

# using Quick Sort Algorithm
#
# def partition_func(i,j,arr):
#     pivot_index = i
#     pivot = arr[pivot_index]
#
#     while i<j:
#
#         while i<len(arr) and arr[i]<=pivot:
#             i = i+1
#
#         while arr[j]>pivot:
#             j = j-1
#
#         if(i < j):
#             arr[i], arr[j] = arr[j], arr[i]
#
#     arr[j], arr[pivot_index] = arr[pivot_index], arr[j]  ## this will put the pivot to its correct place
#     return j
#
# def quick_sort(i,j,arr): # i = start , j = end
#
#     if(i<j):
#
#         a = partition_func(i,j,arr) # a is the final index of the pivot
#
#         quick_sort(i,a-1,arr)
#         quick_sort(a+1,j,arr)
#
#
# arr = [12,32,44,15,-9,-32,-8,-6,5,-4]
# # n= len(arr)
# quick_sort(0,len(arr)-1,arr)
#
# print(arr)


#################################################################################
# finding the UNION and INTERSECTION of elements of 2 arrays
#################################################################################

# simple using two for loops and two variables
#1 USING NEW ARRAY TO PREVENT DUPLICATES

# def UnionArray(arr1, arr2):
#     # Taking max element present in either array
#     m = len(arr1)
#     n = len(arr2)
#     ans = 0
#
#     if m > n:
#         ans = m
#     else:
#         ans = n
#
#     # Finding elements from 1st array
#     # (non duplicates only). Using
#     # another array for storing union
#     # elements of both arrays
#     # Assuming max element present
#     # in array is not more than 10 ^ 7
#     newtable = [0] * (ans + 1)
#
#     # First element is always
#     # present in final answer
#     print(arr1[0], end=" ")
#
#     # Incrementing the First element's count
#     # in it's corresponding index in newtable
#     newtable[arr1[0]] += 1
#
#     # Starting traversing the first
#     # array from 1st index till last
#     for i in range(1, len(arr1)):
#
#         # Checking whether current element
#         # is a duplicate of previous element
#         if newtable[arr1[i]] == 0:
#             print(arr1[i], end=" ")
#             newtable[arr1[i]] += 1
#
#     # Finding only non common
#     # elements from 2nd array
#     for j in range(0, len(arr2)):
#
#         # By checking whether it's already
#         # present in newtable or not
#         if newtable[arr2[j]] == 0:
#             print(arr2[j], end=" ")
#             newtable[arr2[j]] += 1
#
#
# # Driver Code
# if __name__ == "__main__":
#     arr1 = [1, 2, 3, 2, 3]
#     arr2 = [2, 3, 4, 5,1,6]
#
#     UnionArray(arr1, arr2)

### INTERSECTION OF TWO ARRAYS#########
#
# def intersect_array(a,b,m,n):
#
#     intersect = [] # new empty array
#     i = j = 0
#
#     while i<m and j<n:
#             if a[i]==b[j]:
#                 if len(intersect)>0 and intersect[-1]==a[i]: ## intersect[-1] means the last element of array
#                     i+=1
#                     j+=1
#                 else:
#                     print(a[i])
#                     intersect[a[i]]+=1 # or we can do intersect.append(a[i])
#                     j+=1
#             elif a[i]>b[j]:
#                 i+=1
#             else:
#                 j+=1
#     if not len(intersect):
#         return [-1]
#     return intersect
#
# if __name__ == "__main__":
#     arr1 = [1, 2, 2, 3, 4]
#     arr2 = [2, 3, 4, 5, 6, 7]
#
#     l=intersect_array(arr1,arr2,len(arr1),len(arr2))
#     print(l)

## IF THE DIFFERENCE BETWEEN THE TWO ARRAYS IS SIGNIFICANT
# we can do binary search on the larger array for each element of the smaller array
# def union(arr1, arr2, m, n):
#
#     if m > n:  ## we can ensure that the first arr1 is always small
#         temp = arr1
#         arr1 = arr2
#         arr2 = temp
#
#         length = m
#         m = n
#         n = length
#
#     arr1.sort()  # ie, we have sorted the smaller array
#     for i in range(0, m):
#         print(arr1[i], end=',')  # and this array will be present in the final union
#
#     ## now we will search every element of the larger array in the smaller array using binary search
#     for i in range(0, n):
#         if (binary_srch(arr1, 0, m - 1, arr2[i])) == -1:  # ie if the element is not found in the smaller array
#             print(arr2[i], end=',')
#
# def intersection(a,b,n,m):
#     i=j=0
#     intersect=[] # make an empty array
#     if n>m:
#         temp=a # to ensure that the first array is the smaller one
#         a=b
#         b=temp
#
#         length=n # to also keep their lengths correct while swapping
#         n=m
#         m=length
#
#     a.sort()
#     for i in range(0,m):
#         if binary_srch(a,0,n-1,b[i])!=-1:
#             intersect.append(b[i])
#     print(intersect,end='')
#
#
# def binary_srch(arr,l,r,x): # l=left index , r= right index, x= element
#     if r>=l:
#         mid = (r + l)//2
#
#         if arr[mid]==x:
#             return mid
#
#         if arr[mid]>x: #ie, the element is smaller than mid  so we do search in left array
#             return binary_srch(arr,0,mid-1,x)
#         else: # search in the right array
#             return binary_srch(arr,mid+1,r,x)
#
#     return -1 # ie element is not found in the array
#
#
#
#
# if __name__=='__main__':
#     arr1=[1,2,5,4,7]
#     arr2=[4,5,2,7,1,9,8]
#     union(arr1,arr2,len(arr1),len(arr2))
#     intersection(arr1,arr2,len(arr1),len(arr2))


####################################################################

# USING HASHING FOR INTERSECTION AND UNION ###### NOT SOLVED YET
# def findPosition(a, b):
#     v = len(a) + len(b);
#     ans = [0] * v;
#     zero1 = zero2 = 0;
#     print("Intersection :", end=" ");   #####################  NOT SOLVED YET
#
#     # Iterate first array
#     for i in range(len(a)):
#         zero1 = iterateArray(a, v, ans, i);
#
#     # Iterate second array                 ################# NOT SOLVED YET
#     for j in range(len(b)):
#         zero2 = iterateArray(b, v, ans, j);
#
#     zero = zero1 + zero2;
#     placeZeros(v, ans, zero);
#     printUnion(v, ans, zero);
#
#
# # Prints union of arr1[0..n1-1] and arr2[0..n2-1]
# def printUnion(v, ans, zero):
#     zero1 = 0;                           ################### NOT SOLVED YET
#     print("\nUnion :", end=" ");
#     for i in range(v):
#         if ((zero == 0 and ans[i] == 0) or
#                 (ans[i] == 0 and zero1 > 0)):
#             continue;
#         if (ans[i] == 0):
#             zero1 += 1;
#         print(ans[i], end=",");
#
#
# def placeZeros(v, ans, zero):
#     if (zero == 2):
#         print("0");
#         d = [0];
#         placeValue(d, ans, 0, 0, v);
#     if (zero == 1):
#         d = [0];
#         placeValue(d, ans, 0, 0, v);
#
#
# # Function to iterate array
# def iterateArray(a, v, ans, i):
#     if (a[i] != 0):                ############################## NOT SOLVED YET
#         p = a[i] % v;
#         placeValue(a, ans, i, p, v);
#     else:
#         return 1;
#
#     return 0;
#
#
# def placeValue(a, ans, i, p, v):
#     p = p % v;
#     if (ans[p] == 0):
#         ans[p] = a[i];
#     else:                            ######################  NOT SOLVED YET
#         if (ans[p] == a[i]):
#             print(a[i], end=",");
#         else:
#             # Hashing collision happened increment
#             # position and do recursive call
#             p = p + 1;
#             placeValue(a, ans, i, p, v);
#
#
# # Driver code
# a = [7, 1, 5, 2, 3, 6];
# b = [3, 8, 6, 20, 7];
# findPosition(a, b);

########################################################################################

# Implementation of Hashing with Chaining in Python

# m = Length of Hash Table
# n = Total keys to be inserted in the hashtable
# Load   =    lf = n / m
# factor
#
# Expected time to search = O(1 + lf)
#
# Expected time to insert / delete = O(1 + lf)
#
# The time complexity of search insert and delete is O(1) if lf is O(1)

# Function to display hashtable
# def display_hash(hashTable):
#     for i in range(len(hashTable)):
#         print(i, end=" ")
#
#         for j in hashTable[i]:
#             print("-->", end=" ")
#             print(j, end=" ")
#
#         print()
#
#
# # Creating Hashtable as
# # a nested list.
# HashTable = [[] for _ in range(10)]
#
#
# # Hashing Function to return
# # key for every value.
# def Hashing(keyvalue):
#     return keyvalue % len(HashTable)
#
#
# # Insert Function to add
# # values to the hash table
# def insert(Hashtable, keyvalue, value):
#     hash_key = Hashing(keyvalue)
#     Hashtable[hash_key].append(value)
#
#
# # Driver Code
# insert(HashTable, 10, 'Allahabad')
# insert(HashTable, 25, 'Mumbai')
# insert(HashTable, 20, 'Mathura')
# insert(HashTable, 9, 'Delhi')
# insert(HashTable, 21, 'Punjab')
# insert(HashTable, 21, 'Noida')
#
# display_hash(HashTable)


###############################################################################
################  rotate an array by one  ##############
###############################################################################

#
# arr= [1,5,6,4,3]
# n= len(arr)              ################## this method is by swapping the elements
# i=0
# j=n-1
# #
# # while(i<j):
# #     arr[i],arr[j]=arr[j],arr[i]
# #     i+=1
# #     j-=1
# #
# # print(arr)
#
# ######## METHOD 2 #########
#
# x = arr[n-1]
# for i in range(n-1,0,-1):   ## keep the order of indexes in mind
#     arr[i]=arr[i-1]
#
# arr[0]= x
#
# print(arr)


################################################################################

# LARGEST SUM CONTIGUOUS SUBARRAY  = KADANE'S ALGORITHM

###############################################################################




# def maxSubArraySum(a, size):
#     max_so_far = a[0]
#     max_ending_here = 0
#
#     for i in range(0, size):
#         max_ending_here = max_ending_here + a[i]
#         if (max_so_far < max_ending_here):
#             max_so_far = max_ending_here
#
#         if max_ending_here < 0:
#             max_ending_here = 0
#     return max_so_far
#
#
# # Driver function to check the above function
# a = [-2, -3, 4, -1, -2, 1, 5, -3]
# print("Maximum contiguous sum is", maxSubArraySum(a, len(a)))


############################################################################################

############################################################################################

# Check if a key is present in every segment of size k in an array

#######################################################################

# def solution(arr,x,k,n):
#     i=0
#
#     a = n%k
#     while i<n-a:
#         j=0        #for every new i, initialize the j as 0 and move upto j<k
#         while(j<k):
#             if arr[i+j]==x:
#                 break           # if x is found in the subsegment
#             j+=1     # if the no. is not found , increment j
#
#         if j==k:          # ie, no. was not found in the subsegment
#             return False
#
#
#         i+=k   # for next while iteration we start we next subsegment
#
#     if i==n:                # ie, the loop is complete and 'n' is a perfect multiple of 'k'
#         return True
#
#     ## but if the 'n' is not a perfect multiple
#
#     j =n-a  # reset the 'j' for last subsegment
#
#     while j<n:
#         if arr[j]==x:
#             break
#
#         j+=1
#
#     if j==n:
#         return False   # ie x not found in the last subsegment
#
#     return True
#
#
#
# arr = [3,5,2,4,9,3,1,7,3,11,3,12,14,3]
# x=3
# k=4
# n=len(arr)
# sol = solution(arr,x,k,n)
# if sol:
#     print("yes")
#
# else:
#     print('no')


# Python 3 program to find
# the every segment size of
# array have a search key x

# def findxinkindowSize(arr, x, k, n):
#     i = 0
#     while i < n:
#
#         j = 0
#
#         # Search x in segment
#         # starting from index i
#         while j < k:
#
#             if arr[i + j] == x:
#                 break
#
#             j += 1
#
#         # If loop didn't break
#         if j == k:
#             return False
#
#         i += k
#
#     # If n is a multiple of k
#     if i == n:
#         return True
#
#     j = i - k
#
#     # Check in last segment if n
#     # is not multiple of k.
#     while j < n:
#         if arr[j] == x:
#             break
#
#         j += 1
#
#     if j == n:
#         return False
#
#     return True
#
#
# # Driver Code
# if __name__ == "__main__":
#
#     arr = [3, 5, 2, 4, 9, 3,
#            1, 7, 3, 11, 12, 3,14,2]
#     x, k = 3, 3
#     n = len(arr)
#
#     if (findxinkindowSize(arr, x, k, n)):
#         print("Yes")
#     else:
#         print("No")
#
# # This code is contributed
# # by ANKITRAI1
#



##########################################################################
##########################################################################

# correct method for finding out semi-prime number

# def check_prime(n): #for checking weather prime or not
#     if n > 1:
#         if n == 2: return True
#         for i in range(2,n):
#             if n % i == 0:
#                 return False
#                 break
#         return True
#     return False
# def primeproduct(m): #for checking wheather prime product or not
#     if m >= 0:
#       for i in range(1,m):
#         if m%i == 0 and check_prime(i) and check_prime(m//i):
#             return True
#             break
#     return False
#
# a = primeproduct(9)
# print(a)

##################################################################################
##################################################################################
#     TO OMIT ALL THE OCCURANCES OF A CHARACTER 'c' FROM A STRING 's':

# def delchar(s,c):
#     end = ''
#     if len(c)==1:
#         s=s.replace(c,'')
#
#         print(s)
#     else:
#         print(s)
#
# s= input()
# c=input()
# delchar(s,c)

################################################################################
# q3
#   TO PRINT THE ALTERNATE ITEMS FROM THE LIST1 AND THEN LIST2 AND THEN MAKE A FINAL LIST

# def shuffle(l1,l2):
#     minimum= min(len(l1),len(l2))
#     i=0
#
#     list1 = []
#     while i<minimum:
#
#         list1.append(l1[i])
#         list1.append(l2[i])
#         i+=1
#     if len(l1)!=minimum:
#         for i in range(minimum,len(l1),1):
#             list1.append(l1[i])
#     elif len(l2)!=minimum:
#         for j in range(minimum,len(l2),1):
#             list1.append(l2[j])
#     return list1
#
#
# a = shuffle([0],[1,3,5])
# print(a)

########################################################################################
#         TO CHECK IF A NUMBER IS SEMIPRIME -----> ie,  A NUMBER IS A PRODUCT OF TWO PRIME NUMBERS

# def primefactor(n):
#     for i in range(2,n):
#         if n%i==0:
#             break
#
#     else:
#         return True
#
# def primeproduct(n):
#     for i in range(2,n+1):
#         if n%i==0:
#             if primefactor(i) and primefactor(n//i):
#                 return True
#             else:
#                 return False
#
# a = primeproduct(2)
# print(a)

#####################################################################################################

################## TAKING 2D ARRAY AS AN INPUT  ######################################################
# r= int(input("no. of rows "))
# c= int(input("no. of columns "))
# arr = [[(item for item in int((input().split('\n')).split(''))) for j in range(c)]for i in range(r)]

# print(arr)



#  1 2 3
#  2 3 4
#  5 6 7

# list1 = [[1,2,3],[2,3,4],[3,4,5]]
#
# for i in range(len(list1)):
#
#     if i==0 or i%2==0:
#         for j in range(0,len(list1[i]),1):
#             print(list1[i][j])
#
#
#     elif i%2!=0:
#         for j in range(len(list1[i])-1,-1,-1):
#             print(list1[i][j])
#
#     i+=1

# class Solution:
#     # @param A : tuple of list of integers
#     # @return a list of integers
#     def spiralOrder(self, A):
#         lst = []
#         t = 0
#         b = len(A) - 1
#         l = 0
#         r = len(A[0]) - 1
#         dir = 0
#         while(t <= b and l <= r):
#             if(dir == 0):
#                 for i in range(l,r+1):
#                     lst.append(A[t][i])
#                 t += 1
#             elif(dir == 1):
#                 for i in range(t,b+1):
#                     lst.append(A[i][r])
#                 r -= 1
#             elif(dir == 2):
#                 for i in range(r,l-1,-1):
#                     lst.append(A[b][i])
#                 b -= 1
#             elif (dir == 3):
#                 for i in range(b,t-1,-1):
#                     lst.append(A[i][l])
#                 l += 1
#             dir = (dir + 1) % 4
#         return lst


# A=[[1,2,3],[2,3,4],[5,6,7]]
# result = Solution()
# print(result.spiralOrder(A))
#########################################################################################################################


###################################################################33

# pick from both sides
#####################################################################

# A= [1,2,3,4,5,6,-7,8]
# n=len(A)
# b= 3
# sum1=0
# maxim=0
# start = b
# end= n
# for i in range(0,b):
#     sum1=sum1+A[i]
#     maxim=sum1
#
# while start>=0 and end>=n-b:
#     sum1= sum1- A[start-1]
#     start = start-1
#
#     sum1 = sum1+A[end-1]
#     end = end-1
#     maxim=max(maxim,sum1)
#
# print(maxim)
#
#
# ############################################################################################################################
# # to find minimum and maximum
# A =[1,2,-3,4,5,6,7]
# m=len(A)
# minim=A[0]
# maxim=A[0]
# for i in range(0,m):
#     if A[i]>maxim:
#         maxim=A[i]
#     if A[i]<minim:
#         minim=A[i]
#
# print(maxim+minim)
#
# ########################################################################################################################
# ########################################################################################################################
#   # BINARY SEARCH ALGORITHM ###################
#
# def bst(arr,start,end,v):
#     n= len(arr)
#     mid=(start+end)//2
#
#     if end-start==0:
#         return -1
#
#     if v==mid:
#         return mid
#     else:
#         if v<mid:
#             bst(arr,0,mid,v)
#         elif v>mid:
#             bst(arr,mid+1,n,v)


########################################################################################################################

############## A FUNCTON TO ENSURE THAT THE DIFFERENCE BETWEEN TWO CORRESPONDING INTEGERS IN THE LIST IS STRICTLY INCREASING #########################

# def expanding(l):
#     diff = 0
#     for i in range(1, len(l)):
#         a = max(l[i], l[i - 1])
#         b = min(l[i], l[i - 1])
#
#         if (a - b) > diff:
#             diff = a - b
#         elif (a - b) <= diff:
#             return False
#     return True
# l=[1,3,7,2,-3]
# a = expanding(l)
# print(a)


#######################################################################################################################
########################################################################################################################

# FUNCTION TO PRINT THE SUM OF SQUARES OF ODD NUMBERS AND SUM OF SQUARES OF EVEN NUMBERS SEPARATELY

# def sumofsquares(l):
#     sumodd=0
#     sumeven=0
#
#     for i in range(0,len(l)):
#         if l[i]%2==0:
#             sumeven = sumeven+ (l[i])**2
#         elif l[i]%2!=0:
#             sumodd = sumodd +(l[i])**2
#
#     return (sumeven,sumodd)


########################################################################################################################
########################################################################################################################

#####  PRINT TRANSPOSE OF A MATRIX

#1 Method = IN-PLACE for SQUARE MATRIX only, otherwise for all other cases we will have to use an extra array for transpose

n=4
# def transpose(A):
#
#     for i in range(n):
#         for j in range(i+1,n):
#             A[i][j],A[j][i]=A[j][i],A[i][j]
#
# A=[[1,1,1,1],
#    [2,2,2,2],
#    [3,3,3,3],
#    [4,4,4,4]]
# # m=4
#
# transpose(A)
# for i in range(n):
#     for j in range(n):
#         print(A[i][j],'',end='')
#
#     print() #prints a new line
#
#
#
# ###########################################################################
#
# #2 METHOD 2 = FOR RECTANGULAR MATRICES WITH DIFFERENT NUMBER OF ROWS AND COLUMNS
# #              USING A SEPARATE ARRAY FOR STORING THE TRANSPOSE
#
# def transpose(A,B,row,col):
#     for i in range(col):
#         for j in range(row):
#             B[i][j]=A[j][i]
#
#
#
#
# A = [[1,1,1,1],[2,2,2,2],[3,3,3,3]]
# row=len(A)
# col=len(A[0])
# B=[[0 for x in range(row)]for y in range(col)]  # we have already set the col and row order for the transpose matrix
#
# transpose(A,B,row,col)


#########################################################################################################################
#########################################################################################################################

# MERGE SORT
# def merge(arr,start,mid,end):
#     temporary = [0] * (end - start + 1)
#
#     i=start
#     j=mid+1
#     k=0
#
#
#     while i<=mid and j<=end:
#         if arr[i]<=arr[j]:
#             temporary[k]=arr[i]
#             k+=1
#             i+=1
#         else:
#             temporary[k]=arr[j]
#             k+=1
#             j+=1
#
#     while i<=mid:
#         temporary[k] = arr[i]
#         k += 1
#         i += 1
#
#     while j<=end:
#         temporary[k] = arr[j]
#         k += 1
#         j += 1
#
#     for l in range(start,end+1):
#         arr[l]=temporary[l-start]
#     return arr
#
#
#
# def mergesort(arr,start,end):
#
#     if start<end:
#
#         mid = (start + end) / 2
#         mergesort(arr,start,mid)
#         mergesort(arr,mid+1,end)
#         merge(arr,start,mid,end)
# arr=[1,20,3,10,5,6,12,8]
# i=0
# j=len(arr)-1
# a = mergesort(arr,i,j)
# print(a)


# example of merge sort in Python
# merge function take two intervals
# one from start to mid
# second from mid+1, to end
# and merge them in sorted order
# import sys
# sys.setrecursionlimit(10000)
# def merge(Arr, start, mid, end):
#     tempo = [0] * (end - start + 1)   # we are writing end-start because the index can also start from 1 , then it willl be a problem deciding the end
#     i= start
#     j=mid+1
#     k=0
#     while i <= mid and j <= end:
#         if Arr[i] <= Arr[j]:
#             tempo[k]=Arr[i]
#             k+=1
#             i+=1
#
#         else:
#             tempo[k] = Arr[j]
#             k+=1
#             j+=1
#
#     while(i <= mid):
#         tempo[k] = Arr[i]
#         k += 1
#         i += 1
#     while(j <= end):
#
#         tempo[k] = Arr[j]
#         k += 1
#         j += 1
#
#     for i in range(start, end+1):
#         Arr[i] = tempo[i-start]
#     return Arr
#
#
# # Arr is an array of integer type
# # start and end are the starting and ending index of current interval of Arr
#
# def mergeSort(Arr, start, end):
#     if(start < end):
#         mid = (start + end) // 2
#         mergeSort(Arr, start, mid)
#         mergeSort(Arr, mid+1, end)
#         return merge(Arr, start, mid, end)
#
#
# Arr=[1,20,3,10,5,6,12,8]
# i=0
# j=len(Arr)-1
# a = mergeSort(Arr,i,j)
# print(a)


##################################################################################
#################################################################################

# Quick Sort Algorithm

##################################################################################3

# def partition(arr, low, high):
#
#     i = (low - 1)  # index of smaller element
#     pivot = arr[high]  # pivot
#
#     for j in range(low, high):
#
#         # If current element is smaller than or
#         # equal to pivot
#         if arr[j] <= pivot:
#             # increment index of smaller element
#             i = i + 1
#             arr[i], arr[j] = arr[j], arr[i]
#
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return i + 1


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low --> Starting index,
# high --> Ending index

# Function to do Quick sort
# def quickSort(arr, low, high):
#     if low < high:
#
#         # pi is partitioning index, arr[p] is now
#         # at right place
#         pi = partition(arr, low, high)
#
#         # Separately sort elements before
#         # partition and after partition
#         quickSort(arr, low, pi - 1)
#         quickSort(arr, pi + 1, high)
#
#     # Driver code to test above
#
#
# arr = [10, 7, 8, 9, 1, 5]
# n = len(arr)
# quickSort(arr, 0, n - 1)
# # print("Sorted array is:")
# for i in range(n):
#     print(arr[i])
    # print("%d" % arr[i]),

# def mystery(l):
#     if l == []:
#         return(l)
#     else:
#         return(mystery(l[1:])+l[:1])
#
# a= mystery([22,34,18,57,92,45])
# print(a)
#
# pairs = [ (x,y) for x in range(5,1,-1) for y in range(4,1,-1) if (x+y)%3 == 0 ]
# print(pairs)



##########################################################
################################################################

# start = int(input('enter test case number' ))
# for i in range(start):
#     n= int(input('enter number '))
#     for j in range(n):
#         x=input('enter string ').upper()
#         if x=='U':
#             print('D')
#         elif x=='L':
#             print('L')
#         elif x=='R':
#             print('R')
#         elif x=='D':
#             print('U')
#
#
# ###########################################################################3
# ###########################################################################
#
# ## Backtracking N-QUEENS - PYTHON CODE
#
# ###############################################################
# ################################################################
#
#
# def initialize(n):
#   for key in ['queen','row','col','nwtose','swtone']:
#     board[key] = {}
#   for i in range(n):
#     board['queen'][i] = -1
#     board['row'][i] = 0
#     board['col'][i] = 0
#   for i in range(-(n-1),n):
#     board['nwtose'][i] = 0
#   for i in range(2*n-1):
#     board['swtone'][i] = 0
#
# def printboard():
#   for row in sorted(board['queen'].keys()):
#     print((row,board['queen'][row]))
#
# def free(i,j):
#   return(board['row'][i] == 0 and board['col'][j] == 0 and
#           board['nwtose'][j-i] == 0 and board['swtone'][j+i] == 0)
#
# def addqueen(i,j):
#   board['queen'][i] = j
#   board['row'][i] = 1
#   board['col'][j] = 1
#   board['nwtose'][j-i] = 1
#   board['swtone'][j+i] = 1
#
# def undoqueen(i,j):
#   board['queen'][i] = -1
#   board['row'][i] = 0
#   board['col'][j] = 0
#   board['nwtose'][j-i] = 0
#   board['swtone'][j+i] = 0
#
# def placequeen(i):
#   n = len(board['queen'].keys())
#   for j in range(n):
#     if free(i,j):
#       addqueen(i,j)
#       if i == n-1:
#         return(True)
#       else:
#         extendsoln = placequeen(i+1)
#       if extendsoln:
#         return(True)
#       else:
#         undoqueen(i,j)
#   else:
#     return(False)
#
# board = {}
# n = int(input("How many queens? "))
# initialize(n)
# if placequeen(0):
#   printboard()
#
#
# #####################################################################
# ## N queens ------------> ALL SOLUTIONS
#
# def initialize(n):
#     for key in ['queen', 'row', 'col', 'nwtose', 'swtone']:
#         board[key] = {}
#     for i in range(n):
#         board['queen'][i] = -1
#         board['row'][i] = 0
#         board['col'][i] = 0
#     for i in range(-(n - 1), n):
#         board['nwtose'][i] = 0
#     for i in range(2 * n - 1):
#         board['swtone'][i] = 0
#
#
# def printboard():
#     for row in sorted(board['queen'].keys()):
#         print((row, board['queen'][row]), end=" ")
#     print("")
#
#
# def free(i, j):
#     return (board['row'][i] == 0 and board['col'][j] == 0 and
#             board['nwtose'][j - i] == 0 and board['swtone'][j + i] == 0)
#
#
# def addqueen(i, j):
#     board['queen'][i] = j
#     board['row'][i] = 1
#     board['col'][j] = 1
#     board['nwtose'][j - i] = 1
#     board['swtone'][j + i] = 1
#
#
# def undoqueen(i, j):
#     board['queen'][i] = -1
#     board['row'][i] = 0
#     board['col'][j] = 0
#     board['nwtose'][j - i] = 0
#     board['swtone'][j + i] = 0
#
#
# def placequeen(i):
#     n = len(board['queen'].keys())
#     for j in range(n):
#         if free(i, j):
#             addqueen(i, j)
#             if i == n - 1:
#                 printboard()
#             else:
#                 extendsoln = placequeen(i + 1)
#             undoqueen(i, j)
#
#
# board = {}
# n = int(input("How many queens? "))
# initialize(n)
# if placequeen(0):
#     printboard()
#

####################################################################
###################################################################


###############################################################################

# def repeated(l):
#     count = 0
#     list1 = []
#     for i in range(len(l)):
#         if l[i] in list1:
#             count += 1
#         else:
#             list1.append(l[i])
#
#     return count
# a = repeated([1,17,22,17,23,17])
# print(a)


# def sublist(l1,l2):
#     s1=" ".join(str(i) for i in l1)
#     s2=" ".join(str(i) for i in l2)
#     if s1 in s2:
#         return True
#     else:
#         return False
#
# l1 =[1,2,3]
# l2=[1,1,2,3,4]
# a=sublist(l1,l2)
# print(a)

# def alldistinct(a,b,c):
#     result = False
#     if a!=b:
#         if b!=c:
#
#             if a!=c:
#                 result=True
#
#     else:
#         result=False
#
#
#     return(result)
#
# a=alldistinct(13,15,14)
# print(a)
#
# i = 1
# count = 0
# while (True):
#     new = input()
#     if new == '':
#         break
#
#     if i == 1:
#         s1 = [char for char in new]
#         count = len(s1)
#
#
#     elif i != 1:
#         s2 = str(new)
#         s3 = [char for char in s2]
#
#         for i in range(len(s1)):
#             for j in range(len(s3)):
#                 if s3[j] == s1[i]:
#                     count += 1
#
#     i = i + 1
# print(count)

a = 'there'
l1 = tuple(char for char in a)

# print(l1)
for i in range(len(l1)):
    s1 = ''.join(str(l1[i]))
    print(s1)



