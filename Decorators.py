def my_decorator(func):
    def wrapper():
        print("print before the function runs ")
        func()
        print("print after the function runs ") 
    return wrapper 

@my_decorator  
def ayush():
    print("Hello World") 

ayush()  