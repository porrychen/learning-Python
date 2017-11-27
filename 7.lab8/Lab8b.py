# Global constants
MONKEYS = 3
DAYS = 7

# The main function.
def main():
    # Create a two-dimensional list.
    foodList = []
    for i in range(MONKEYS):
        monkey = []
        for j in range(DAYS):
            # Initialize all array elements to zero
            monkey.append(0)
        foodList.append(monkey)

    # Input the food eaten by each monkey
    getFood(foodList)
    # Print the contents of the list
    displayFood(foodList)
    print()

    # Display the average amount of food eaten
    print('The average amount of food eaten is', format(calcAverage(foodList), '.1f'))

# The getFood function.
def getFood(foodList):
    for i in range(MONKEYS):
        print('Monkey ', i + 1, '.', sep = '')
        for j in range(DAYS):
            food = -1
            while food < 0.0:
                try:
                    food = float(input('  Please enter the food eaten for day ' + str(j + 1) + ': '))

                    # check input is non-negative
                    if food < 0.0:
                        print('⭕ ERROR: The food eaten must be zero or larger!')
                    else:
                        foodList[i][j] = food
                except ValueError:
                    print('⭕ ERROR: Must be a valid number of the food eaten!')
                    food = -1

# The displayFood function.
def displayFood(foodList):
    for i in range(MONKEYS):
        print()
        # display title
        if i == 0:
            for j in range(DAYS):
                print(' ' * (10 - len('Day' + str(j + 1))) + 'Day' + str(j + 1), end = '')
            print()
        # display coloums
        for j in range(DAYS):
            print(format(foodList[i][j], '10.1f'), end = '')
    print()

# The calcAverage function.
def calcAverage(foodList):
    sum = 0
    for i in range(MONKEYS):
        for j in range(DAYS):
            sum += foodList[i][j]
    return sum / (MONKEYS * DAYS)

# Call the main function.
main()
