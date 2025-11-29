print("Welcome to the average of 3 numbers machine..")
continue_option = 'y'
while continue_option =='y':
    print("Please enter three numbers a,b,c")
    a = float(input(""))
    b = float(input("")) #These need to be floats in order for this to work. 
    c = float(input(""))
    print("The average comes to", (a*b*c)/3)
    continue_option = input("would you like to go again? y/n " )
print("Thanks for using the program")