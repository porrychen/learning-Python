# This program allows the user to choose various
# conversions from a menu.

# Global constants for menu choices
LOOK_UP = 1
QUIT = int(9)


# The main function.
def main():
    # Initialize a variable for the user's choice.
    choice = 0

    while choice != QUIT:
        choice = get_menu_choice()
    else:
        print('Bye! See you next time!')



# The get_menu_choice function displays the menu
# and gets a validated choice from the user.
def get_menu_choice():
    count = 0;
    menudata = get_menu_data();

    # display a Menu
    print()
    print(' Menu')
    print('------------------------------')
    for key, value in sorted(menudata.items()):
        print(key, ') ', value, sep = '')
    print()

    # Get the user's choice.
    while count <= 0 or choice < LOOK_UP or choice > QUIT:
        try:
            choice = int(input('Enter a valid choice: '))

        except ValueError:
            print('ERROR: a choice must be valid numbers.')
            print()
            choice = 0

        count += 1

    # return the user's choice.
    return choice;

# The get_menu_data function makes the menu's data
def get_menu_data():
    return {'1': 'Miles to kilometers',
                '2': 'Fahrenheit to Celsius',
                '3': 'Gallons to liters',
                '4': 'Pounds to kilograms',
                '5': 'Inches to centimeters',
                '9': 'Quit the program'}

# Call the main function.
main()
