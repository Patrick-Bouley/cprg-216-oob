# If no return function is presetn, then there is no output for those functions, we cant assign these to other variables

# A function header is the entire line of code with the def function. def square(): <-- that whole line is the header, the colon is included. Could also be called a signature
# The function cubby, is everything that comes after. like the variables/arguments

# Input-output function
def square(x):
    return x**2
    # return None # Is equivilanet to no return 

# Input but no output functions. Print is an example of these
# def write_to_file(filename, msg):
#     fid = open(filename, 'w')
#     # w is for writting, r is for reading, a is for appending
#     fid.write(msg)
#     fid.close()
# This function but doesn't have a return value, so there is no output. despite it creating or opening a file

# No input but has an output
print("Hello, please enter your name")
# name = input()

# No input no output
def print_welcome():
    print("Hello, welcome to the software")

# Memory/Stack/Heap
# Thge stack usually stores easy variables 
# The heap usually stores lists, directories, and variables that are more complex. 
# Memory is sorted into bites, and those bites store the variables. we assign a piee of memory to a variable when we create them. 
# Each variable has a name, a value, a size, and a type. All of these create the address of that variable to the memory we assigned it to. The address can also be called by a refrence. This means it will change the value of the originall information, instead of creating a copy and using more memory
# More complex data structures use more than 1 bite to store that information (lists, directories, tuples, sets...etc)

# call by refrence vs call by value

# This is a call by value
y = 5
def add_one(x):
    x = x+1
    return x
print(y)
print(add_one(y))
print(y)

# This is a call by refrence

data = [1,2,3]
def add_one(list):
    data.append(4) # Data in each time are treated like single values.

print(data)
add_one(data)
print(data)

# Arguments

def read_file(file):
    fid = open(file, 'r')
    text = fid.readline() # This reads the first line
    return text

msg = read_file('hola')
print(msg)

# Positional, Must be written exactly how its implemented in your function. value 1, value 2. Must always be written that way unless you over ride it in the code you are writting
# Variable Length arguments. Print has as 
def my_sum(*values): # The * lets us create a variable length argument. its called an appointer, and creates an array. It means this function can take basically an infinit ammount of arguments 
    sum = 0
    for item in values:
        sum += item

    return sum

print(my_sum(1,2))
print(my_sum())
print(my_sum(1))
print(my_sum(1,2,3,4,5,6,7,8,9,10,123,127,800,898))

# Default Arguments. These are optional argumenst that can be changed, but dont need to be as they have a default value already

print("Hello", end = " ") # End is an optional argument that has a default value of \n
print("World")

# def write_config(file='Setting.config'):
#     fid = open(file, "w")
#     fid.write("Screen size: 1900 2800")
#     fid.close()

# write_config()
# write_config(file = "mysetting.config")
# comment this out to not keep rewritting files 

# Global variables are variables that are declared in the main file of the program. if a variable resides outside of a function, it would be considered global, as the entire file can see that variable and use it if its required/called to do so
# You can create a global variable inside a function using the global keyword. as long as the variable is defined inside that function and uses the global keyword. Ex
# def square(x):
#     global x
#     x = 5
#     return x**2
# Local files are variables that are defined inside a function. Meaning only that function has access to that variable, it will not exsist in the main file and cant be called by other functions
# Using the above example, if you take out the "global x" keyword. x becomes a variable that is only locally known inside that function. Meaning we cannot call for x outside that function

global_var = 1

def print_local_global():
    global inside_global
    inside_global = 3
    local_var = 5
    print("Inside Global", inside_global)
    print("Local Variable" , local_var)
    print("Outside Global", global_var)
print_local_global()
print(global_var)
print(inside_global)
# print(local_var) # This provides an error as the local var is defined inside a function. This print is outside of that function, so it doesnt know what the variable is, as it has not been defined gloabally 

def c_to_f(C_temp):
    f = (9/5) * C_temp+32
    return f

def f_to_c(F_temp):
    c = (F_temp-32)*(5/9)
    return c

option = input("What Temperature do you want? F/C ").lower()
if option == "f":
    C_temp = float(input("Input the temperature in Celcius\n"))
    print("The temperature in F is: ", c_to_f(C_temp))
else:
    F_temp = float(input("Input the Temperature in F\n"))
    print("The Temperature in C is: ", f_to_c(F_temp))

print("Enjoy the weather!")