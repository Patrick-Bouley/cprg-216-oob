print(format(12345.6789, ",.2f"))
print(format(12345.6789, "14.2f"))
# The 14 infront menats the input will be shifted by how ever much that number is, digits shift from the left while strings will shift from the right
print(format(12345.6789, ".2e"))
print(format(0.5, "%"))
print(format(123, "d"))
print(format(-123, "7d"))
print(format("Hello", "10s"))

x= 4
y= 2.3
print('The variable of y has the value of {1} and x has the value of {0}' .format(x, y))
# we can use the 0, 1, 2.... to determine how we input the variables of the format in any order we want. 
# We implement the way we want to format these variables in the {} brackets after a : EX {0:.2f}

num = 12345.6789
print("{:.2f}" .format(num))
print("{:,.2f}" .format(num))
print("{:.2e}" .format(num))

Percent = 0.5
print("{:%}" .format(Percent))

Digits = 123 
print("{:d}" .format(Digits))

Neg = -123
print("{:7d}" .format(Neg))

Text = "Hello"
print("{:10s}" .format(Text))

num = 12345.6789
print("This is just the decimal version of the variable: {0:.2f} \nThis is the comma and decimal version: {0:,.2f} \nThis is a scientific version {0:.2e} " .format(num))
# In this case you still have to define what you are trying to format, even though there is only one variable you are working with. 

print(f"x is {x} y is {y:.4f}")
# This makes it so the placeholder becomes whatever variable you enter into it, while still letting you format how you want it to appear inside the {}

name1 = "John"
name2 = "Sarah"
name3 = "Adam"
print(f"The name is {name1:>20}")
print(f"The name is {name2:<20},")
print(f"The name is {name3:^20},")
# The >20 will allow us to shift it to the left like you would with digits
# the <20 will add that many spaces after the characters, creating a huge gap that we can see with thge "," at the end
# The ^20 will center the text in the middle of those 20 spaces


'''
This is a program to format the CAD table
'''

yesterday_val = 0.7588
today_val = 0.7479

change = today_val - yesterday_val

print("{:>10s}{:>10s}".format("Date",  "Rate"))
print("{:>10s}{:>10s}".format("====",  "===="))
print("{:>10s}{:>10.4f}".format("Yesterday",  yesterday_val))
print("{:>10s}{:>10.4f}".format("Today",  today_val))
print("{:>10s}{:>10.4f}".format("Change",  change))
# We use 10 for the shift because "yesterday" is our largest string with 9 characters. so we add one extra space to make it look nice
# We have to keep the formats similar to ensure the layout is uniform and the layout is consistent. 
print("\n")
print(f'{"Date":>10s}{"Rate":>10s}')
print(f'{"====":>10s}{"====":>10s}')
print(f'{"Yesterday":>10s}{yesterday_val:>10.4f}')
print(f'{"Today":>10s}{today_val:>10.4f}')
print(f'{"Change":>10s}{change:>10.4f}')