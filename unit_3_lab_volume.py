def volume(rectangle):
    volume = x * y * z
    return volume

x = 0
y = 0
z = 0

Calculate = True
print("Welcome to the Recangular Box Volume Calculator!\n" "Please Input the Length, Width, and Height (in cm) of the rectangle you would like to Calculate! One item at a time", end = "\n")
while Calculate == True:
    rectangle = x, y, z
    x = int(input("Length:\n"))
    y = int(input("Width:\n"))
    z = int(input("Height:\n"))
    print("The volume of the rectangle is:", + volume(rectangle), "ccm")
    Calculate = input("Would you like to Calculate another rectangle? y(yes)/n(no) \n").lower()
    if Calculate == 'y' or Calculate =='yes':
        Calculate = True
    else:
        Calculate = False
print("Thanks for using my program!")

