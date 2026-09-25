""" A lambda function is an anonymous, inline function defined using
the lambda keyword......."""

#  Squaring a Number ->>> 
square = lambda x:x**2 
print(square(5))  

""" The argument 4 is passed in x. you can also have multiple
arguments and you can also include If - Else expressions """  

check_even = lambda x : "Even" if x %2==0 else "odd"
print(check_even(7))  