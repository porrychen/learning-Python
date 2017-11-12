# Program to convert Feet to miles

# The main function.
def main():

    # initialize variables
    feet = -1.0
    miles = 0.0

    # when feet is less than 0
    while feet < 0:
        try:
            # get the number of feet
            feet = float(input('Please input the number of feet: '))

            # validate the feet
            if feet < 0:
                print('\n⛔ ERROR: Number of feet cannot be negative.', end = '\n\n')
            else:
                feetToMiles(feet)

        except ValueError:
            feet = -1.0
            print('\n⛔ ERROR: Number of feet must be valid numbers.', end = '\n\n')

    # display ending words
    print()
    print('⬐-----------------------------⬎')
    print('    Bye! See you next time!    ')
    print('⬑-----------------------------⬏')

# The feetToMiles function for coverting feet to miles.
def feetToMiles(feet):
    # Calculate and display the corresponding number of miles
    miles = feet / 5280
    print(feet, 'feet is', miles, 'miles')
    print()

# Call the main function.
main()
