import random

# # # Functions like this dont need to return a value, as we are just essentially making a shortcut for a message that we want to print at some point later on. 
# # def welcome_message():
# #     print("Welcome to the program!")
# # name = input("What is your name?:")
# # def say_hello(name):
# #     print("Hello,", name)
# # say_hello(name)
# # welcome_message()

# def line_of_characters(char, repeats):
#     line = str(char) * repeats
#     print(line)

# line_of_characters('x', 30)
# line_of_characters(5, 15)

# def square_root(num):
#     y = num**0.5
#     return y

# print(square_root(25))

# def get_option():
#     options = ['yes', 'no', 'Yes', 'No', 'y', 'n', 'Y', 'N']
#     option = 'abc'
#     while option not in options:
#         option = input('Would you like to continue? Yes/No\n')
#     print('You decided to say', option)

# # The Header has a set of words that are mandatory for creating a function. def and then the Function Name (which can be anything, usually we name them something that relates to what we are doing), plus the () at the end followed by a colon :
# def square(num):
#     '''
#     This fuction takes one argument
#     our argument is x
#     the purpose is to square whatever argument is inputed
#     '''
#     sq = num**2 # num*num also works for finding a square, but the ** is a more direct translation of it
#     return sq # You need to define the entire function and what it does. just having it be x**2 will not actually hold a value and make this function essentially do nothing. so we have to return the value for the function to hold some sort of value

# print(square.__doc__)
# # In order to get this to work, you need to input the multi line comment as the very first thing under the def function. must be indented into the code as well so it "resides" under the def function

# number = 3
# y = square(number)
# # Without the return y in the def function code, This doesnt actually hold a value. it still does the process but doesnt save the output
# print(y)
# print(square(5))
# z = 3 + square(3)
# print(z)

# # For functions that take more than one variable, we can help define them with "if" statements. laying out how we want the function to interact with the information we provide it
# def my_max(x, y):
#     if x>y: # we check the value of x and compare it to y, depending on the bigger value, that is the one we want to return
#         ma = x
#     else:
#         ma = y
#     return ma

# def my_min(x, y):
#     if x<y: # check the value of x and compare it to y. we want to take the smallest value and return that as our min
#         mi = x
#     else:
#         mi = y
#     return mi

# print(my_max(3,4))
# print(my_min(3,4))
# print(my_max(7,1))
# print(my_min(7,1))

# # We can use functions to shorten code, if we are using the same thing over and over again for the same purpose. 
# # we originally had 40 lines of code. but since we defined the function we were using, we shortnend it to 14 lines.

# def new_max():
#     print("Please enter 2 numbers")
#     x = int(input())
#     y = int(input())
#     if(x>y):
#         print(x)
#     else:
#         print(y)

# print(new_max())
# print("Lets pause here")
# print(new_max())
# print(new_max())
# print(new_max())
# print("Lets stop here")


# def print_info(name, year_of_birth):
#     print("Hello", name, "You are now", 2025-year_of_birth, "years old")

# name = "John"
# yob = 2000

# print_info(name, yob)

def print_line_of_characters(ch, num):
    line = ch * num
    print(line)

for i in range(1,21):
    print_line_of_characters('*', i)

for i in range(21,0,-1):
    print_line_of_characters('*', i)

# function types (there are 3 types)

# function takes arguments (inupt), and gives an output (return)
def sqrt(x):
    return x**(1/2) #This is the output
y = sqrt(4) # evaluates to 2
print(y)
m = 9
n = sqrt(m) # evaluates n to = 3
print(n)
print(sqrt(25))

# Function takes arguments (input), and does not give an output
x = print(3)
print(x)

def print_welcome(name):
    print("Hello", name, "Welcome to my program")

# def write_to_file(file, msg):
#     fid = open(file, 'w')
#     fid.write(msg)
#     fid.close()

# write_to_file("Demo.txt", "Hello world")

y = print_welcome("Patrick")
print(y)
# Print takes an argument. but doesnt actually return anything 

# Function doies not take arguments, and does not give an ouput
def anon_welcome_msg():
    print("Welcome to the Program")

anon_welcome_msg()

# Function does not take an argument, but will return an output
# def generate_random_number():
#     return random.randint(1,100)

# for i in range(0,10):
#     print(generate_random_number(), end = ' ')


#  A mutable object is passed through the argument of a function

# pass by value, vs pass by reference 

def add_one(x): # Pass by value. essentially takes a copy of the value and oes its argument
    x = x+1
    print(x)

d=5 #we cant change the original value
add_one(d)
print(d)

def modify_list(data): # pass by reference. allows us to change the original value and keep it implimented in that value, instead of creating a copy and keeping the orginal the same  
    data.append(5)
    print(data)

nums = [1, 2, 3, 4]
print(nums)
modify_list(nums)
print(nums)

# Function Arguments 
# Positional, These arguments mean that they are written in a certain way, and the info has to be provided in the exact same way ie (x,y) the first argument will always be x, and the second will always be y
# Option are argumenst that can be skipped in writting, because they have default arguments to go with them already ie print("hello", "How are you?" sep=" " end = " ") sep and end are optional because they have defaukt argumenst, so we dont have to write them out, unless we want to change them