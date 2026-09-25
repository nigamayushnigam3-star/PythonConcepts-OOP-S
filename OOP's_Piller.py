# #  Inheritance ->>
# Inheritance allows one class to acquire the properties and methods of
# another class. This avoids writing the same code again and again, and
# makes your codebase much cleaner.

# . Parent class (also called base class) contains common, shared features
# . Child class (also called derived class) inherits everything from the parent
# . Child class can also add its own new attributes and methods on top
# . Changes made in the parent class automatically reflect in child classes
# . Real life example: Animal class has eat() and sleep(). Dog and Cat
# inherit these, and Dog adds bark(), Cat adds meow()

class Animal:
    def eat(self):
        print("I m eating ") 

    def sleep(self):
        print(" I m sleeping ")

class Dog(Animal):
    def bark(self):
        print(" dog is barking ")

dog = Dog()
dog.bark()
dog.eat()
dog.sleep()


class Animal:

    def __init__(self,name:str,age:int):
        self.name=name
        self.age=age
        # __init__ ->> its a constructor , whenever the object will be created its automaticallly called ...

    def eat(self):
        print("I m eating ")  

    def sleep(self):
        print(" I m sleeping ")

class Dog(Animal):
    def bark(self):
        print(" dog is barking ")

    def display(self):
        print(f"Name is {self.name} & age is {self.age}") 

dog = Dog('sheru',5)
dog.bark()
dog.eat()
dog.sleep()
dog.display()

cat = Dog("sheri",10)
cat.display() 


class Animal:

    def __init__(self,name:str,age:int):
        self.name=name
        self.age=age
        # __init__ ->> its a constructor , whenever the object will be created its automaticallly called ...

    def eat(self):
        print("I m eating ") 

    def sleep(self):
        print(" I m sleeping ")

class Dog(Animal):
    def __init__(self):
        print("Dog init")


    def bark(self):
        print(" dog is barking ")

    def display(self):
        print(f"Name is {self.name} & age is {self.age}")

dog = Dog()
 
#  O/P->> dog init 
# jbbhi m  dog = Dog() eske through display chane jaunga toh sirf yhi init chalega uppper wala nhii...




class Animal:

    def __init__(self,name:str,age:int):
        self.name=name
        self.age=age
        # __init__ ->> its a constructor , whenever the object will be created its automaticallly called ...

    def eat(self):
        print("I m eating ") 

    def sleep(self):
        print(" I m sleeping ")

class Dog(Animal):
    def __init__(self,name:str,age:int,breed:str):
        super().__init__(name,age)
        #  super().__init__ ->> ye jis class me hoga uske upper wale class se jo bhi variable hm pass krenge uski value lake de dega
        self.breed = breed 
        print(" This is dog init ")  

    def bark(self):
        print(" dog is barking ")

    def display(self):
        print(f"Name is {self.name} & age is {self.age} & {self.breed}")

dog = Dog("cherry",5 ,"inde")
dog.display()
 

##########################################################
# Polymorphism -->>>>

# Poly means many, morph means forms, Polymorphism allows the same method name to behave differently depending on which object calls it. This makes your code highly flexible and extensible.
# . Same method name works differently for different classes
# . You don't need to remember multiple method names for similar actions
# . Method Overriding: Child class provides its own version of a parent's method
# Real life example: A "draw()" method on a Circle draws a circle, on a Rectangle it draws a rectangle - same name, different behavior.


# class Animal:
#     def move(self):
#         print(" Animal is running ")

# class Dog(Animal):
#     def walk(self):
#         print("Dog is walking") 

# dog=Dog() 
# dog.move()
# Output->> Animal is running 


class Animal:
    def move(self):
        print(" Animal is running ")

class Dog(Animal):
    def move(self):
        print("Dog is walking") 

dog=Dog() 
dog.move()
# output ->>> dog is walking bcoz the dog's method will be overide the animal method bcoz the calling object is Dog's object 
# That's called polymorphism 

#############################################################################################################################
# Encapsulation -->>     
# Encapsulation is the technique of hiding the internal details of an object and allowing access only through controlled methods such as getters and setters.
# Basically its are mainly used during Data Hiding ....
# Encapsulation is about protecting the internal data of a class. You control
# what the outside world can see and what it cannot. This prevents
# accidental modification of important data.

# . Data and methods that operate on that data are bundled together
# inside a class
# . Sensitive data is marked private so it can't be accessed directly from outside
# . Access is given through controlled methods called getters anci setters
# . Makes code more secure and predictable 
# . Real life example: ATM machine you car check balance
# and withdraw, but you can't access the bank's internal
# system directly
# Abstraction is about reducing complexity. You expose only the necessary
# details to the user and hide all the complicated internal logic. The user
# doesn't need to know how things work inside, just that they work.

# class Bank:
#     def __init__(self,name:str,balance:int):
#         self.name:str  = name
#         self.balance:int = balance

#     def deposite(self,amount:int):
#         self.balance += amount
#         print(f"Amount deposited, current balance ={self.balance}\n")

#     def withdraw(self,amount):
#         if amount > self.balance:
#             print("Not enough money in bank \n")
#         else:
#             self.balance -= amount
#             print(f"amount withdrawn,current balance ={self.balance}\n")

# acc = Bank("Ayush",1000)
# acc.deposite(500)
# acc.balance = 10000 # dekho ye direct balance ki value change kr de rha h , jo ki shi nhi h , esiliyr hm basically apne variable ko private bnayenge ... "__variable name"
# acc.withdraw(500)


class Bank:
    def __init__(self,name:str,balance:int):
        self.name:str  = name
        #Private Variable 
        self.__balance:int = balance

    def deposite(self,amount:int):
        self.__balance += amount
        print(f"Amount deposited, current balance ={self.__balance}\n")

    def withdraw(self,amount):
        if amount > self.balance:
            print("Not enough money in bank \n")
        else:
            self.__balance -= amount
            print(f"amount withdrawn,current balance ={self.__balance}\n")

acc = Bank("Ayush",1000)
acc.deposite(500)
acc.balance = 10000 # dekho ye direct balance ki value change kr de rha h , jo ki shi nhi h , esiliyr hm basically apne variable ko private bnayenge ... "__variable name"
acc.withdraw(500)
            

    
    