#  They’re special keywords in Python used in function definitions to
# accept a flexible number of arguments 

# Args -> Having Multiple positional arguments and becomes a tuple 
def fun(*args): 
    print(" Args: ",args)

fun(1,2,3)  


# kwargs -> having multiple keyword arguments and becomes a dictionary 
def func(**ayush):
    print(ayush)

func(name="ayush",age=21) 


# combination of both args and kwargs 
def new(*args,**kwargs):
    print("Args",args)
    print("Kwargs",kwargs)

new(1,2,3,name="ayush",age=21) 