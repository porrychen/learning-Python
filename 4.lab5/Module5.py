'''
    Write a program that consists of 2 functions, a main function and a function named calcTotalCost:

    The main function will do the following:

    Gets the following information from the user: car price, registration cost, and sales tax amount
    This information is then passed to the calcTotalCost function.
    The calcTotalCost function will do the following:

    Calculate the total cost of the car.
    Display the total cost to the user with an appropriate label
'''
# The main function.
def main():
    # Gets the following information: car price, registration cost, and sales tax amount
    car_price = float(input('Please enter a car price: '))
    registration_cost = float(input('Please enter a registration cost: '))
    sales_tax = float(input('Please enter a sales tax amount: '))

    # Call the calcTotalCost function
    calcTotalCost(car_price, registration_cost, sales_tax)

# The calcTotalCost function.
def calcTotalCost(car_price, registration_cost, sales_tax):
    # Calculate the total cost of the car
    total_cost = car_price + registration_cost + sales_tax

    # Display the total cost to the user with an appropriate label
    print('The total cost of the car is ', '$' + format(total_cost, ',.2f'))

# Call the main function.
main()
