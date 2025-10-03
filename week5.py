'''
Review of if statement

if condition :
    statement 1
    statement 2
    statement 3
elif
    statement 1
    statement 2
    statement 3
else
    statement 1
    statement 2
    statement 3

print()

# Now we are talking about loops
if condition: #these run only once if the condition is true
    statement 1
    statement 2

while condition: #these run as long as the condition is true
    statement 1
    statement 2

    if condition: This one will run once as it meets the condition of being true
    print("Hello World")

    

condition = True

while condition: #This will run forever cause the condition is true, Control + C will interupt if its running
    print("Hello World")
    print("This is the second line")
#These will continue to print both lines as long as the condition is true. constantly checking to make sure the requirements are met after every secon d line
#we can add a condion to be false after the loop is done to ensure it doesnt constatly print lines
    condition = False

#if condition was equal to false, it wouldnt print anything at all

counter = 0
condition = counter <10

while condition:
    print("counter")
    counter += 1 #this will take the counter, and add 1 to it for every time it runs. 
    condition = counter < 10 #you have to include this so the condition also continues to update within the loop

counter = 0
while counter<10 : #This makes the counter the condition, which would update in real time with the loop
    print(counter)
    counter += 1

print("done")

These are for sums
index = 0
counter = 1
while counter<101 :
    index += counter
    counter += 1
print(index)

box = 0
apples = 1
while apples <= 100:
    box += apples
    apples += 1
print(box)

#This is for factorials 
#Factorial has to start at 1 for this to work, as 0 multiplied by anything equals 0
factorial = 1
counter = 1
while counter <= 5:
    factorial *= counter
    counter += 1
print(factorial)
'''

# ax^2 + b x + c = 0
# x1 = -b+sqrt(b^2 - 4ac)/2a
print("Welcome to the quadratic equation solver..")
continue_option = 'y'
while continue_option =='y':
    print("Please enter three numbers a,b,c\n")
    a = float(input("\n"))
    b = float(input("\n")) #These need to be floats in order for this equation to work. 
    c = float(input("\n"))

    x1 = None
    x2 = None
    if a == 0:
        if b == 0:
            print("No real solution...")
        else:
            x1 = x2 = -c/b
            print(x1, '\t', x2) 
    else:
        det = b**2 - 4 * a * c
        if det >= 0:
            x1 = (-b - det ** 0.5)/(2 * a)
            x2 = (-b + det ** 0.5)/(2 * a)
            print(x1, '\t', x2) 
        else:
            print("No real solution")
    continue_option = input("Would you like to solve another equation? y/n\n")