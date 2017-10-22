# Program to convert Feet to miles

# initialize variables
feet = 0.0
miles = 0.0

# get the number of feet
feet = float(input('Please input the number of feet: '))

# validate the feet
if feet < 0:
    print('Number of feet cannot be negative.')
else:
    # Calculate and display the corresponding number of miles
    miles = feet / 5280
    print(feet,'feet is', miles,'miles')


