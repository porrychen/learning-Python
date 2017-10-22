# Program to convert Feet to miles

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
            print()
            print('🔴  Number of feet cannot be negative.')
            print()
        else:
            # Calculate and display the corresponding number of miles
            miles = feet / 5280
            print(feet,'feet is', miles,'miles')
            print()

    except ValueError:
        feet = -1.0
        print()
        print('🚫  Number of feet must be valid numbers.')
        print()
