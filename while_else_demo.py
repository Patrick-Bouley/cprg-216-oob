'''
counter = 0
while counter<6:
    print(counter)
    counter += 1
else:
# This form of else is very redundant. the condition gets met and will still print "done" regardless of the else input beingt there
    print("done")

i =1
while i < 11:
    j = 1
    while j <11:
        print(j, "x", i, "= ", j*i)
        j += 1
    i += 1
print("done")
# This will print the times table for 1, all the way up to 1 x 10
# we added j as a nested loop, to change what we multiply i by, basically creating the times table for number 1 to 10, up to being multiplied by 10

print(list(range(1,11)))
# Range will print numbers from the first number selected, up to the last number selected - 1. IE 11 wont print
# By default, the first number is 0, if no other number is provided
print(list(range(11)))
# so this will print the same thing as the first range we made
print(list(range(5,50,5)))
# This will range numbers between 5 and 50 (exc;uding 50), by counting by 5

for n in range(1,11):
# n is the variable for the statement, it will take the number of said range and make it that variable. In a "while" loop we donmt necessarily know when
# when it will end, but there is a hidden flag looking to see if the condition is still true, and will end once that condition is changed. 
# "for" loops will run for however long we give it for a statement. 
    print(n)
'''
for n in range(1,11):
    if n ==5:
        continue
    for m in range(1,11):
        if m == 7:
            break
        # this break will stop the for loop that it is in, but will continue with the other loop that houses all the information 
        # This is a nested example for a for loop, basically doing the same thing we set up for the first 1 - 10 times table
        print(n, 'x', m, '=', n*m)


# Wew are working with a list in the assignment, and are going over it now
'''
x = 1

weather = [24, 16, 35]
# we use [] to indicate that we are using a list
# a dictionary uses {}
# it stores these numbers as an aray

week = ['sat', 'sun', 'mon', 'tue','wed', 'thur', 'fri']
numbers = [1,2,3,4,5,6,7]
print(week)
print(numbers)

for number in numbers:
    print(number)

for day in week:
    print(day)

sum = 0

for number in numbers:
    sum += number

print(sum)
'''
gpas = []

gpas.append(3.4)
gpas.append(3.2)
gpas.append(4.0)
gpas.append(3.7)
# append can be implimented with a user input

print(gpas)

sum_gpa = 0
for gpa in gpas:
    sum_gpa += gpa
print(sum_gpa/4)

# we are talking about strings now
# Strings are essentially an array of words or numbers (with no values) 
# print can take seveal argumanets at once, one of which is the text you put in it "hello"
print("hello", "world")
print("hello" + "world")
# These are two seperate arguments that print is taking

msg = 'hello' + 'world'
print(msg)
# this makes it so print is tyaking only one arguement instead.

print("hello") #sep ' ' and end '\n' sep is by default set to just be a space, and end is default to start a new line, or end the current line and go to the next
print("world")

print("hello","world","hey", sep = ',', end = '\t') #Sep here will seperate the words just with a comman, while the end, will no longer end the line, but just input a 'tab' key, allowing the second line of code to be printed on the same line as well.
print("world")

# Now we talking about the format function
# this function takes 2 arguments, the first one being a string or float, the second wil lbe the string of the format we want

x = format(23434.232323, '.2f')
print(x)

print(format(23434.232323, '.3f'))
# the 3f takes whatever we give, and changes the display of it to something else. 3f makes it so we only get 3 digits after the decimal point
# can use ',.2f', '1 4,.2f' '.2e' '%' 
print(format(23434.232323, '18.2f'))
# we can use this for formatted printing for stuff like collums and tables 

print(format(0.4, '%'))
print(format(2, '7d')) # this will shift any digit, 7 units to the right, showing that there4 is empty space before the digit
print(format('hello', '7s')) #strings start from the left and print to the right, ie, there will be empty characters after hello that we cannot see, but they are there

course = 'cprg-216'
section = 'A'

print('We have a new course and its name is: {} section: {}'.format(course, section))
# this is very similar to printf the {} is a place holder for how you want to format whatever you have in the format section


