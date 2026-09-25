#  All of these Comprehensions are used to create List, Dictionary
# and set. But you don’t have to use multiple lines of code for loops
# and If-Else statements.  

#  List Comprehentions :-->>>  for baad me lgta h expression phle likha jata h 
labels = [ "Even" if x %2==0 else "Odd" for x in range(5)]  
print(labels) 

#  Dict Comprehention :__>>> 
even = {x:x*x    for x in range(10) if x%2==0 }   
print(even) 

#  Set Comprehention :-->>> 
unique_even_squares = {x*x for x in range(10) if x %2 ==0}  
print(unique_even_squares)  