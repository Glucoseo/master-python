age = 25 #integerr variable
name = "alice" #initiliaze string variables using ""s
is_active = True #boolean-typed variables - they can contain either False or True
#Dynamic types
x = 10 #integer
x = "Heline" #String
print(type(x))  # <class 'str'>
#How does python allocate memory for data
a = [1, 2, 3] # a list called a
b = a # b is now a second name tag assigned to the same exact list

b.append(4)
print(a) # [1, 2, 3, 4]
print(id(a), id(b)) #2877083465984 2877083465984
#== is used to check if the variables are the same
#"is" is used for checking if the variables point to the same exact object in memory check Info/isoperator.py for more info
#Use id() to see the actual memory address a variable point to

#Multiple assignment
X_pos, Y_pos, Z_pos = 1, 2, 3

#Swapping variables
Number_1 = 5
Number_2 = 10
Number_1, Number_2 = Number_2, Number_1
print(Number_1, Number_2) #10 5

#Unpacking
coordinates = (45.0, -90.0)
lat, lon = coordinates #lat stands for latitude while lon stands for longtitude

#Scope and the LEGB rule (Local, Enclosing, Global, Built-in)
#Scope determines where in the code the object can be see and used
# Local - insied the current function
# Enclosing - inside any enclosing(parent) funciton
# Global - at the top level of the module/script
# Built-in pythons pre-defined names like len() or print()
x2 = 'globla'

def outer():
    x2 = "enclosing"

    def inner():
        x2 = "local"
        print(x2)  #Python finds the Local 'x' first.
    inner()
    print(x2)
outer()
print(x2)
#Global and nonlocal
count = 0

def increment():
    global count #Tells to modify the global one not to define any
    count +=1

#Type hinting
user_age: int = 30
is_logged_in: bool = False
emails: list[str] = ["test@test.com","admin@test.com"]
