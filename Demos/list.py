x = 3
# this is a single variable
week = ['sat', 'sun', 'mon', 'tue', 'wed', 'thur', 'fri']
num = [1, 2, 3, 4, 5, 6]
data = [1.2, 1.4, 4.2, 3.5, 8.9, 7.9]
conditions = [False, True, True, False, True]
# These are all lists, we can use lists for things like strings, variables, floats and boolean expressions.
# You can use something like data[2]=4.5 to change the data outside of thee list without actually editing the list itself

print(week)
# This will print the entire list as is
print(week[4])
# This lets us pring something from that list, using a number to represent where it it in that list.
# The [] is where that number goes, starting from 0 

print(data)
print(data[3])
header = 'Squares'
print(f"{header:>20}")

for i in num:
    square = i**2
    print(i, square)
# This lets us print the list on a seperate line each, instead of all on one
# going from one item to the next, in order of how they are written

# print(week[0])
# print(week[1])
# print(week[2])
# this is reduntant and can just be written in a for loop

for i in range(0, 6): # Range generates a list [0, 1, 2, 3, 4, 5]
    print(data(i))

# List Functions 
print(range(5))
list_numbers = list(range(5))
print(list_numbers)
# The list functions takes an item and makes a list out of it

# len function
nums_length = len(num)
week_length = len(week)
data_length = len(data)
# This item takes a list, and defines the length of that list, it returns as an int for its size
print(f"length of num is {nums_length}")
print(f"length of week is {week_length}")
print(f"length of data is {data_length}")

# count function
n = conditions.count(True)
print(f"The value True is repeated {n} Times")
n = conditions.count(False)
print(f"The value False is repeated {n} Times")
n = num.count(1)
print(f"The value 1 is repeated {n} Times")
# This function is not length, but will count how many times that condition is in the list

# append function, We are using this in the first assignment
temperatures = [21]
temperatures.append(23)
for n in range(1,21):
    temperatures.append(n)

print(temperatures)

sequence = []
print(sequence)
print(f"length of sequence is {len(sequence)}")
sequence.append(0)
for n in range(1,101):
    sequence.append(n)

print(sequence)

# delete a value from the list
# del or remove or pop

del week[0]
# This removes the first value in the list that has been chosen
print(week)

week.remove('fri')
# This lets you remove a specific value from the list
print(week)

week.pop(2)
# This basically does the same thing as del
print(week)


# Index in lists
# The index usually starts at 0, but in python, you can make an index start from the end
print(num)
print(num[0]) #This makes you start at the first index of the list
print(num[-1], num[5]) #In python, this lets you start at the end of the list ie 6
print(num[-2], num[4]) #This is the second last item in the index, ie 5

for day in week:
    print(day)

nums = [1, 3, 4, 4, 5]
for nubs in nums:
    print(nubs)


# list concatenation
weekend = ['Sat', 'Sun']
weekdays = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri']
week = weekdays+weekend
print(week)
# This basically appends the first list into the second list

students = ['Sam', 'Sarah', 'John', 'Tom']
student_name = input("What is the student name?:")
if student_name in students:
    print("Student is in the sytsem already")
else:
    print("Sorry, that student is not in the system")

# We use in here to check if the name already exists in the list, making it so we dont repeat items, or add mulltiple of the same thing

if student_name not in students:
    print("Sorry, that student is not in the system")
else:
    print("Student is in the sytsem already")

random_list = [5,2,6,1,3,8,12,3,-1]
sorted_list = sorted(random_list)

print(random_list)
print(sorted_list)

#A shallow copy function
m1 = [1,2,3]
m2 = m1
print(m1)
print(m2)
m2[2]=4
print(m1)

#a deep copy function
n1 = [1,2,3,4]
n2 = n1.copy()
n2[2]=-1
print(n1)
print(n2)

# Strings join and split
# Join takes an array of strings and makes one list out of them
# Split takes the list and makes an array out of them 
words = ["I", "am", "alright"]
Text = " ".join(words)
Text += ", and you?"
print(Text)
new_words = Text.split(",")
print(new_words)

# Min and max
print(min(sorted_list))
print(max(sorted_list))
print(sum(sorted_list))

# Clear
random_list.clear()
print(random_list)

# Count vs index
print(sorted_list.count(13))
print(sorted_list.index(12))

# append vs insert
print(sorted_list)
sorted_list.append(13) # Append will just add the new item at the end of the list.
print(sorted_list)
sorted_list.insert(5,4) # Insert lets us insert something at that specific point in the list. 
# The first digit is the location, while the sendon one is th eone one we wanna add

# Slicing
print(sorted_list[:5])
print(sorted_list[5:])
print(sorted_list[1:4])