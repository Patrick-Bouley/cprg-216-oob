import random
NUM_DICE_TO_ROLL = 8
SEED = 2183

def roll_dice(num):
    rolls = []
    for i in range(num):
        rolls.append(random.randint(1, 6))
    return rolls
    # Return a list of 'num' random dice rolls between 1 and 6.
    # using the "for i in range" loop. I is unused, meaning that what ever the input would be for num, is how many times the dice is rolled.
 
def most_repeats(values):
    # Return the highest number of repeating values in the list.
    repeats = 0
    for r in values:
        count = values.count(r)
        if count > repeats:
            repeats = count
    return repeats
 
def main():
    random.seed(SEED)
    # We use the random.seed(SEED) to make a file that matches the output. You can get rid of this to make a completly random seed everytime the program runs
 
    while True:
        # Roll the dice
        roll = roll_dice(NUM_DICE_TO_ROLL)
 
        # Determine the number of repeats based off of what was rolled
        repeats = most_repeats(roll)
        # Prints that number for the user to see
        print(f"Your roll of {roll} contains {repeats} of a kind.")
 
        # Ask user whether they want to continue or quit
        again = input("Do you want to roll again (Y/N)? ").strip().lower()
        if again != 'y':
            break
 
if __name__ == "__main__":
    main()

# This lets us structure code so that The main program runs only when the script is executed, not when imported.
# Other scripts can import this function without triggering the main logic.