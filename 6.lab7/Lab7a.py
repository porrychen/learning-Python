# Global constants for menu choices
QUIT = 9

# The main function.
def main():
    # Initialize a variable for the user's choice.
    choice = 0

    while choice != QUIT:
        # display a menu and return a choice number
        choice = get_menu_choice()

        # Initialize variables for the conversion
        euros = -1.0
        dollars = -1.0

        # verify the choice
        if choice == 1:
            while euros < 0.0:
                euros = get_euros()
            # Convert euros to dollars
            euros_to_dollars(euros)
            
        elif choice == 2:
            while dollars < 0.0:
                dollars = get_dollars()
            # Convert dollars to euros
            dollars_to_euros(dollars)

    print('⬐------------------------------⬎')
    print(' ⭐  Bye! See you next time! ⭐ ')
    print('⬑------------------------------⬏')

# The get_euros function for inputing a number of euros
def get_euros():
    try:
        euros = float(input('Please input a number of euros: '))

        if euros < 0.0:
            print('€ Number of euros must be non-negative! \n')
    except ValueError:
        print('⭕ ERROR: Must be a valid number of euros! \n')
        euros = -1.0
    return euros

# The euros_to_dollars function for converting euros to US dollars
def euros_to_dollars(euros):
    dollars = euros * 1.14
    print(format(euros, '.2f'),'euros is', format(dollars, '.2f'),'US dollars')

# The get_dollars function for inputing a number of US dollars
def get_dollars():
    try:
        dollars = float(input('Please input a number of US dollars: '))

        if dollars < 0.0:
            print('Number of US dollars must be non-negative! \n')
    except ValueError:
        print('⭕ ERROR: Must be a valid number of US dollars! \n')
        dollars = -1.0
    return dollars

# The dollars_to_euros function for converting US dollars to euros
def dollars_to_euros(dollars):
    euros = dollars / 1.14
    print(format(dollars, '.2f'),'US dollars is', format(euros, '.2f'),'euros')

# The get_menu_choice function displays the menu
# and gets a validated choice from the user.
def get_menu_choice():
    count = 0
    menudata = get_menu_data()
    keys = []

    # display a Menu
    print()
    print('⬓ Menu ⬓')
    print('-------------------------------')
    for key, value in sorted(menudata.items()):
        keys.append(int(key))
        print(key, ') ', value, sep = '')
    print()

    # Get the user's choice.
    while count <= 0 or choice not in keys:
        if count > 0:
            print('⭕ ERROR: The choice must be in', str(keys)[1:-1])
            
        try:
            choice = int(input('Enter a valid choice: '))

        except ValueError:
            print('⭕ ERROR: a choice must be valid numbers.')
            print()
            choice = 0

        count += 1

    # return the user's choice.
    return choice

# The get_menu_data function makes the menu's data
def get_menu_data():
    return {'1': 'Euros to US Dollars',
            '2': 'US Dollars to Euros',
            '9': 'Quit the program'}

# Call the main function.
main()
