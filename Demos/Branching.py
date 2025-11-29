'''
condition = True
cond = False
#These are boolean expressions
#try to choose a variable name in the form of a question
is_old = True
has_won = False
is_male = True
is_child = False

expression = 3>4
print(expression)

some simple strue or false statements 

x = 5
y = 10
z = 10.01

print(x >= y) will
print(x < y)
print(y > z)
print(z < x)
print(z == y) 
print(y < z)


#Comparison Opererators
# ==, >, >=, <, <=
#all these compare one value to another, generally numbers

#Quadratic equation
a = 0
b = 2
c = 4

x1 = (- b + (sqrt(b**2 - 4 * a * c)))/(2*a)
print((b**2 - 4 * a * c) >= 0)

#if codition
    #print("yes")

print("Hello, welcome to my program")
name = input("What is your age? ")
age = int(name)

is_adult = age >= 18
print(is_adult)
if is_adult:
    print("You\'re an adult!") #this line will be ignored if the condition is false
else:
    print("You\'re not an adult")

#Three forms of if conditions
    #if conditon:
        #one or more indented statements

    #if condition:
        #one or more indented statemetns
    #else
        #one or more indented statemetns

    #if condition:
        #one or more indented statemetns
    #elif condition:
        #one or more indented statemetns
    #else:
        #one or more indented statemetns

print("Welcome to leter grade program")
grade = float(input("Please enter your score: "))

if grade >= 90:
    print("Your letter grade is A")
elif grade >= 80:
    print("Your letter grade is B")
elif grade >= 70:
    print("Your letter grade is C")
elif grade >= 60:
    print("Your letter grade is D")
else: 
    print("Your letter grade is F")

print("Welcome to the party program")
User_Age = input("Please enter your age: ")
age = int(User_Age)
gender = input("Please enter your gender (M/F): ")
if age >= 18:
    print("You are an Adult")
    if gender == str("M"):
        print("You may join the men's party")
    else:
        print("You may join the women's party")
else:
    print("You are nbot an adult")

#Logical Operators: And, Or, not
# age = 17
# gender = 'm'
# condition = gender == m and age >= 18 
# This checks to see if both conditions are met, in order for the conbditoo to be true
# condition = gender == m or age >= 18
# This checks to see if one of the conditons are true 
'''
print("Welcome to the party program")
User_Age = input("Please enter your age: ")
age = int(User_Age)
gender = input("Please enter your gender (M/F): ")
if (age >= 18) and (gender == 'M'):
    print("You are allowed to enter the Mens party")
elif (age >= 18) and (gender == 'F'):
    print("You are allowed to enter the Womens Party")
else:
    print("You are not an adult and cannot enter")

    