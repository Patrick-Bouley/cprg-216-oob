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
'''
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