'''
    Write a program that does the following:

    Have the user enter the rainfall in inches) for each of the 12 months and stores them in a list. These values should be float values.
    Calculates the average monthly rainfall and displays the result to the user.
    Calculates the total rainfall for the year and displays the result to the user
    Displays the highest monthly rainfall and the lowest monthly rainfall to the user.
'''

# Global Constant
MONTH_NAMES = ["January", "Febuary", "March", "April", "May", "June",
          "July", "August", "September", "October", "November",
          "December"]

# The main function.
def main():
    rainfall_list = []

    # The rainfall in inches for each of the 12 months
    input_rainfall(rainfall_list)

    # Calculates the average monthly rainfall, displays the result
    average_rainfall(total_rainfall(rainfall_list), len(rainfall_list))

    # Calculates the total rainfall for the year, displays the result
    total_rainfall(rainfall_list, True)

    # Displays the highest monthly rainfall and the lowest monthly rainfall
    print('The highest monthly rainfall is ', max(rainfall_list), ', and the lowest monthly rainfall is ', min(rainfall_list), sep = '')

# The input_rainfall function.
def input_rainfall(rainfall_list):
    for month in MONTH_NAMES:
        correct = False
        while not correct:
            try:
                # the user enter the rainfall in inches) for each of the 12 months and stores them in a list.
                rainfall = float(input('Please enter the rainfall in inches on ' + month + ': '))
                rainfall_list.append(rainfall)

                correct = True
            except ValueError:
                print('⛔ ERROR: Must be a valid number of the rainfall! \n')

# The total_rainfall function.
def total_rainfall(rainfall_list, isdisplay = False):
    sum = 0
    for value in rainfall_list:
        sum += value

    if isdisplay:
        print('The total rainfall for the year is', sum)

    return sum

# # The average_rainfall function.
def average_rainfall(total_rainfall, count):
    average = total_rainfall / count

    print('The average monthly rainfall is', average)

# Call the main function.
main()
