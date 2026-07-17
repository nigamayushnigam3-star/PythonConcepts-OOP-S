#####################################

# DATA STRUCTURES ->> iTS ARE USED TO SRTUCTURED THE DATA (TO STORE MULTIPLE VALUE IN A SINGLE VARIABLE )  

# LIST->

# 1st way of using index for accessing the data

a = [12,14,15,16,17]

for i in range(len(a)):
    print(a[i])

# 2nd way directly on values 

for i in a:
    print(i)

# methods are just a function which are passes inside the class..

# methods of list -> 

# print(dir(list))

# help(list)

a = [12,14,15,16,17]
a[2] = 18 
print(a)

# read the diff between list and string  

# Some question on list 

# Q} Print + and - element of list 

l=[-8,7,6,-9,10,-12]

print("positive numbers are" )
for i in l:
    if i>=0:
        print(i) # here i me direct value ja rhi h esiliye hm i ikhe h ...

print("negative numbers are" )
for i in l:
    if i<0:
        print(i)

# Q} Mean/avg of list element :-

a = [20,30,40,50,60,70,80]
sum=0
for i in a:
    sum=sum+i
print(sum/len(a))

# Q} find the greatest element and its index too 

l = [12,25,23,24,65,82]

largest = l[0]
index=0

for i in range(len(l)):
    if l[i] > largest:
        largest = l[i]
        index = i

print(f"your largest number is {largest} at index {index}")

# Q} find the second largest element in a list 

l = [12,25,23,24,65,82]

largest = l[0]
sec_largest = l[0]

for i in l:
    if i > largest:
        sec_largest = largest
        largest = i
    elif i > sec_largest:
        sec_largest = i
print(sec_largest , largest)


# Q}-> Check if list is sorted or not ---->>>>>>>>
l = [10,20,30,40,50,60]

for i in range(len(l)-1): # if you go len(a) then its show error out of box
    if l[i]<l[i+1]:
        continue
    else:
        print("your list is not sorted")
        break
else:
    print("your list is sorted") # agr ye break chla tb ye else nhi chalega othervise chalega ye for ke respect me h ....


######### Tuple:- #############

a = (1,2,3,4,5,6)
print(type(a))
print(a[0])
# its have a heterogeneous nature -> store diff types of data structures 
a = (1,1.2,print())
# Acess directly the values 
for i in a:
   print(i)
# by indexing 
for i in range(len(a)):
   print(a[i])

# Two methods only -> index and count method 
t = (8,5,6,9,7,5)
index = t.index(7)
print(index)

num = t.count(7)
print(num)

# NEW AND IMPORTANT CONCEPT TUPLE UNPACKING 

a,b,c,d,e=(7,8,9,4,5) # agr hm ye chahte h ki a me 7 jaye , b me 8 jaye to hm tuple unpacking krenge...
print(a)
print(b)
print(c)
print(d)

# imp
# a=(1) # here type of a will be integer due to this unpacking
# a=(1,) # here type of a will be tuple

####################################################################

# SETS----->>>>>>>

# s = {} # ITS NOT A SET ITS DICTIONARY.....

# Mutable
 
# no-duplicate
s = {1,2,3,4,4,5,5,6,6}
print(s) # its cant so an error its remove the duplicacy the reason behind it is a hash value ...

# sets have no index value i.e unordered , also due to hashing if you print the hash value of single element at two times its will be show two diff diff values ..... 
# s = {1,2,3,4,5,6,}
# print(s[0]) # its shows an error 

# A set can not be traversed using the index values cause it is an unordered and has no index ....

a = {1,8,9,"hello",7,5,4}
for i in a:
    print(i) # jitni br hm esko chaleyege ye alag alag hash value ke karan se alag alag order me print hota h ...

## Set method are important because they provided indexing with the help of hash value .... 

a = {1,2,3,4,5,6}
# print(dir(a)) sows all methods 

a = {1,2,3,4,5,6} # add an element to the set 
a.add(7)
a.remove(2) # remove an element from the set 
a.discard(5) # as remove 
popped_element = a.pop() # remove random element from the set
a.clear() # clear the set
print(a)


#### Operation on two sets ->>

a = {1,2,3,4,5}
b = {4,5,6,7,8,9}
print(a|b)  # union
print(a&b)  # intersection
print(a-b)  # difference
print(a^b)  # symmetric_diff
# aplying compound operations 
b-=a # b=b-a
print(b)

# @ imp -> python me set ke under values store hash ke through hoti h ...

####### Dictionary ->>>

d={} # type <dict>

d = {1:"hello" , 2:50 , 3:40.5, 4:True}
print(type(d))

# its are mutable but we cant change their key bt  we will be change their values...

# Here the elements are printed through his key ->>
d = {1:"hello" , 2:50 , 3:40.5, 4:True}
print(d[3])
# We can also change the value of key but not the key  ->>
d = {1:"hello" , 2:50 , 3:40.5, 4:True}
d[2] = 60
print(d)

# CRUD operation on dic 

d = {10:100 , 20:200, 30:300, 40:400} 

d[10] = 100 # its way for update 
d[60] = 600 # here 60 does not exist so python come this in existance i.e creating...
del d[20] # deletion 
print(d)

# DIC traversing we access both values and key :--

d = {10:100 , 20:200, 30:300, 40:400}

for i in d:
    print(i) # Acess only the key....
 
for i in d:
    print(d[i]) # Acess only the values....

# to check all methods -> help(dict)

# help(dict)

# clear method ->
d = {10:100 , 20:200, 30:300, 40:400}
d.clear() # delete all elements 

# get method 
d = {10:100 , 20:200, 30:300, 40:400}
d2 = d.get(20) # it give the value of key 20 

# for every value of a key 
d = {10:100 , 20:200, 30:300, 40:400}
print(d.items())

# Most Important concept deep copy 

a = [1,2,3,4,5]
b = a # deep esiliye quki b me a depply copy ho jata h 
b[0] = 100
print(a)

# 2nd thing is shalow copy . it means a and b two variable are stored in memory at diff location if we change anything in a then it cant get affect on b and vice versa but in deep copy at a particular location both variable are stored and their changes are in both variables ...

a = [1,2,3,4,5]
b = a.copy() # for shalow copy  we use copy function.. its returns the shallow copy 
b[0] = 100
print(a)

# DICTIONARY QUESTION -->> 
# Q}-> Write a python scripts to merge two dictionaries

d1 = {10:100 , 20:200, 30:300, 40:400}
d2 = {50:500, 60:600, 70:700, 80:800}

for i in d2:
    d1[i] = d2[i] # create a new key-value pair in d1
print(d1)

# Q}-> Write a python program to sum all the items in a dictionary->

d1 = {10:100 , 20:200, 30:300, 40:400}
sum = 0

for i in d1: # yha pe i ke pass sbhi key ki value ayegi 
    sum = sum + d1[i]
print(sum)

# count the frequency of each elements ->>

a = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,6,7,8]

d = {}
for i in a:
    if i in d.keys():
        d[i] = d[i] + 1
    else:
        d[i] = 1
print(d)


# exception handling ->> all read from the book 

a = int(input(" tell your number :- "))
try:
    print(10/a) # Here try check the exception which are raises 

except ZeroDivisionError:
    # yha per hmko pta tha ki zerodivision error ayega age hmko n pta rhe tb ussi ke place pe likhenge ki EXCEPTION AS (ANY VARIABLE) err....
    # print(f" sorry their is an error as {err}")
    print("you can not divide any number by zero ") # Its basically handle this exception 

else:
    print("your division is successfull ") # jb except wala block run nhi krega tbbhi else run karega othervise nhi krega .....

finally:
    print("i will always execute myself ") # ye toh har baar execute ho jayega hi

print(" ok i have done the division ")

# raise exception ->> iske help se hm manually exception raise kr skte h ...
a = int(input(" tell your number :- "))
if a<0:
    raise Exception("sorry no is negative") # here we raise the exception by ourself
print(" completed ") # ess raise ke baad aage ki koi line execcute nhi krti h .....


# FILE HANDLING :----------->>>>>>>

# Accept the gender from the user as char and print the respective greeting message
# Ex - Good Morning Sir (on the basis of gender-->>
a = (input('Enter the gender '))
if len(a) == 1:
   if (a=='M' or a=='m'):
    print("Good morning sir ")
   elif(a=='F' or a=='f'):
    print("Good morning Mam") 
   else:
    print('chosse only M/m for male and F/f for female')
else:
  print('invalid input ')

a = "AYUSH"

for i in range(0,5):
    print(a[i] , end =",")

# Accept an integer and Print hello world n times 
n = int(input("enter a number "))
for i in range(n):
   print("Hello World ")

# Print natural number up to n 
n = int(input("enter the number"))
for i in range(n,1,-1):
    print(i)


######################################################################################################################################################################
