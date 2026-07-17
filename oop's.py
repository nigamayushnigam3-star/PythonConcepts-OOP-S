# OOP'S
# Classes & Objects ->>>
# A class is just a template. It doesn't hold any real data on its own. When you
# create an object from a class that's when actual data gets stored and
# actions can be performed.

# . Class = Blueprint (e.g. design plan of a house)
# . Object = Actual instance built from that blueprint (e.g. the real house)
# . A class defines what attributes (data) and methods (actions) an object will have
# . Multiple objects can be created from the same class, each with their own data
# . Example( "Car" is a class. Your Honda City and your friend's Swift are two different objects

###################################################################
# Class & Object ->>

class Student:
    name=" "
    age=0
    gender=""

s1 = Student()
print(s1) # kuch nhi ayega address ke alwa quki s1 ke under data h ...
print(s1.name)
print(s1.age)
print(s1.gender)
# Data hme set krn hoga 

class Student:
    name=" "
    age=0
    gender=""

s1 = Student()
s1.name="Ayush"
s1.age=21
s1.gender="Male"
print(s1.name)
print(s1.age)
print(s1.gender) 

s2 = Student()
print(s2.name)
print(s2.age)
print(s2.gender) # ye koi value nhi degi quki ek obj dusre obj se relate nhi krti koi interfare nhi krti......
s2 = Student()
s2.name="golu"
s2.age=25
s2.gender="male"
print(s2.name)
print(s2.age)
print(s2.gender)

# Attribute -> variable in class , method -> function in class 

class Student:
    # attributes
    name=" "
    age=0
    gender=""
     
    # Methods 
    def display(self):
        print("This is a display function ")

s1 = Student()
s1.name="Ayush"
s1.age=21
s1.gender="Male"
print(s1.name)
print(s1.age)
print(s1.gender) 
s1.display()
# s2.display()


class Student:
    # attributes
    name=" "
    age=0
    gender=""
     
    # Methods 
    def display(self):
        print(f"My name is {self.name} , age is {self.age} and gender is {self.gender}")

s1 = Student()
s1.name="Ayush"
s1.age=21
s1.gender="Male"
print(s1.name)
print(s1.age)
print(s1.gender) 
s1.display() # yha se hm display call kr rhe h toh uska self ess obj ke location pe aa jayega or hm ussi self ke help se uska data print kr skte h 
# agr app print(s1) kre or print(self) kre toh app notice krenge ki dono ka address same ayega ..
# s2.display()


class Student:
    # attributes
    name=" "
    age=0
    gender=""
     
    # Methods 
    def display(self):
        print(f"My name is {self.name} , age is {self.age} and gender is {self.gender}")

s1 = Student()
s1.name="Ayush"
s1.age=21
s1.gender="Male"
print(s1.name)
print(s1.age)
print(s1.gender) 
s1.display()


class Student:
    # attributes
    name=" "
    age=0
    gender=""
     
    # Methods 
    
    def set_info(self):
        self.name = input("Enter your Name = ")
        self.age = input("Enter your age= ")
        self.gender=input("enter your gender=")

    def display(self):
        print(f"My name is {self.name} , age is {self.age} and gender is {self.gender}")

s1 = Student()
s1.set_info()
s1.display()

s2 = Student()
s2.set_info()
s2.display()  


# parameters-->> 

class Student:

    # attributes
    name=" "
    age=0
    gender=""
     
    # Methods 
    # n :str, a:int ,g:str ->>  n-notation , yhi lega bs or koi nhii..
    def set_info(self , n :str, a:int ,g:str ):
        self.name = n,
        self.age = a,
        self.gender=g,

    def display(self):
        print(f"My name is {self.name}  age is {self.age} and gender is {self.gender}")

s1 = Student()
s1.set_info("ayush",20,"male")
s1.display()


class Student:

    # Methods 
    # n :str, a:int ,g:str ->>  n-notation , yhi lega bs or koi nhii..
    def set_info(self , n :str, a:int ,g:str ):
        self.name = n,
        self.age = a,
        self.gender=g,

    def display(self):
        print(f"My name is {self.name}  age is {self.age} and gender is {self.gender}")

s1 = Student()
s1.set_info("ayush",20,"male")
# attribute htane se ab mera sb field create hoga n ki update  
s1.display()


# Concept of constructor ---->>>>>>>>>>> Contructor is also a method ->> def __init__(Self)...
# Jaise hi hmara object bnta h constructor automatically call ho jata h .....

class Student:
    # Methods:
  
    def __init__(self):
        print("This is Constructor/Initializers")

    def set_info(self , n :str, a:int ,g:str ):
        self.name = n,
        self.age = a,
        self.gender=g,

    def display(self):
        print(f"My name is {self.name}  age is {self.age} and gender is {self.gender}")

s1 = Student()
# o/p->>>This is Constructor/Initializers....
s2 = Student()
# O/P-> This is Constructor/Initializers
# This is Constructor/Initializers


# agr hmse kabhi bhi jo upper se hmne pass kiya h agr vo krn bhul jaye toh error aa jayega ..
# hm ye chah rhe h jaise hi object bne hm data mang le eske liye initializer bnna pdta h ya ussi ko hm constructor bhi bolte h .... 
# s1.display()


class Student:

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self)->None:
        print(f"My name is {self.name} and age will be {self.age} and gender will be {self.gender}")

    def get_age(self)->int:
        # ->int: when you hover jha se call kiya gya h toh dikhega......
        return self.age


s1 = Student("Ayush",20,"male")
# s1.display()
print(s1.get_age())
# jb koi bhi function kuch bhi return nhi krta h tb hm vha none lga dete h...

####################################################################################################################################################################################################################################################################################################################
