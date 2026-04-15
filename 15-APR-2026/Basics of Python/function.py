
#----Basics----

def greet():   #creating fn.
    print("Hello World")
greet() #calling fn.

def greet_user(name):
    return name #send data back to the code that called
print("Hello",greet_user("Zerubba"))
greet()

#----------------

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

print("Add", add(1,2))
print("Subtract", subtract(1,2))
print("Multiply", multiply(1,2))
print("Divide", divide(1,2))
