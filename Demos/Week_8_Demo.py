# Tuples are inmutateable 
# Tuples use () instead of the {}[] that lists and directories use
# The are basically the same as lists, they just cant be changed 

week = ('sun', 'mon', 'tue', 'wed', 'thur', 'fri', 'sat')
# Inmutateable means you cannot change the information in the tuple
empty_tuple = ()
single_tuple = ('s',)
# The tupple needs the comma, it what keeps it different from a string
# 
text = ('string')
# without the comma, it doesnt even become a tuple, but stays as a string

# access elements with index
print(week[2])

#Print thte length
print(len(week))

data = ('Hello', 1, True, 3.4 )
print(data)
for item in data:
    print(item, end='\t')

# data[0] = 'Hola'
# This will not work because you are trying to change the information in a tuple, so we comment it out

# Tuples can take variables and use them as their information in the tuple list.
msg = "Hello World"
num = 2
num1 = 2.4
condition = True
print()
items = (msg, num, num1, condition)
obj1 = items[0]
obj2 = items[1]
obj3 = items[2]
obj4 = items[3]
# we can use a simpler form of this called unpacking
obj1, obj2, obj3, obj4 = items
for item in items:
    print(item, end='\t')

print()
print(obj1,obj2,obj3,obj4)

vowels = {'a','e','i','o','u'}
word = "hello"
for ch in word:
    if ch in vowels:
        print(ch, "is a vowel")
    else:
        print(ch, "Is not a vowel ")
# Sets can not have any items inside of it that repeat. the vowles all have to be different in this case in order to work

# You can change a list (directory and set)  to a tuple and vise versa
vowels = tuple(vowels)
vowels = list(vowels)
# These functions are all you need
num1 = (1,2,3)
num2 = (3,4,5)
num3 = num1+num2
# You cant use the expand or other such functions for lists, when dealing with a tuple. EX num1.extend(num2) this function will not work

# Slicing basically creates a subset of the list you are taking it out of
data = (1,2,3,4,5,6,7)
subset = data[0:2]
print(subset)
# The first number is where you want the index to start, and the second number is where you want it to end in the data
# A different start/end example would be subset = data[3:6] which starts the index at 4, and will end once it reaches the number 6
subset = data[3:6]
print(subset)