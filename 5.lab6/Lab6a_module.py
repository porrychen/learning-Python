# Global constants for menu choices
MILES = 1
FAHRENHEIT = 2
GALLONS = 3
POUNDS = 4
INCHES = 5
QUIT = 9

# The milesToKm function one mile to 1.6 kilometers
def milesToKm(miles):
    return miles * 1.6

# The degreesFToC function one C = (F - 32) * 5/9
def degreesFToC(fahrenheit):
    return (fahrenheit - 32) * 5/9

# The gallonsToLiters function one gallon to 3.9 liters
def gallonsToLiters(gallons):
    return gallons * 3.9

# The poundsToKg function one pound to 0.45 kilograms
def poundsToKg(pounds):
    return pounds * 0.45

# The inchesToCm function one inch to 2.54 centimeters
def inchesToCm(inches):
    return inches * 2.54
    
# The get_menu_choice function displays the menu
# and gets a validated choice from the user.
def get_menu_choice():
    count = 0;
    menudata = get_menu_data()

    # display a Menu
    print()
    print(' Menu')
    print('------------------------------')
    for key, value in sorted(menudata.items()):
        print(key, ') ', value, sep = '')
    print()

    # Get the user's choice.
    while count <= 0 or choice < MILES or choice > QUIT:
        try:
            choice = int(input('Enter a valid choice: '))

        except ValueError:
            print('ERROR: a choice must be valid numbers.')
            print()
            choice = 0

        count += 1

    # return the user's choice.
    return choice

# The get_menu_data function makes the menu's data
def get_menu_data():
    return {'1': 'Miles to kilometers',
            '2': 'Fahrenheit to Celsius',
            '3': 'Gallons to liters',
            '4': 'Pounds to kilograms',
            '5': 'Inches to centimeters',
            '9': 'Quit the program'}
