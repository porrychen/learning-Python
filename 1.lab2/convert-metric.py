# This program allows the user to choose various
# conversions from a menu.

class Convertor():
    # The __init__ method initializes
    def __init__(self):
        # US measures
        self.__us = 0
        self.__us_name = ''
        self.__us_name_plural = 's';
        # metric measures
        self.__metric = 0
        self.__metric_name = ''
        self.__metric_name_plural = 's';

    # The input_us_measures method enter a number for convertor
    def input_us_measures(self, us_name, metric_name):
        self.__us_name = us_name;
        self.__metric_name = metric_name;
        print('Please tell me how many ', self.__us_name, 's you want converted to ', self.__metric_name, 's.', sep = '')
        try:
            self.__us = float(input('Enter a number:'))
            if self.__us != float(1) and self.__us != float(0):
                self.__us_name += self.__us_name_plural
        except ValueError:
            print('ERROR: must be a valid number.')
            print()

        return self.__us

    # The output_metric_measures method displays result
    def output_metric_measures(self):
        if self.__metric != float(1) and self.__metric != float(0):
            self.__metric_name += self.__metric_name_plural

        result = ' ' + str(self.__us) + ' ' + self.__us_name + ' is equal to ' + format(self.__metric, ',f') + ' ' + self.__metric_name + ' ';
        pix_result = ''
        siff_result = ''
        for i in range(0, len(result)):
            pix_result += '↓'
            siff_result += '↑'
        print(pix_result, result, siff_result, sep = '\n')

        self.__us_name_plural = 's';
        self.__metric_name_plural = 's';

    # The miles_to_kilometers method one mile to 1.6 kilometers
    def miles_to_kilometers(self):
        self.input_us_measures('mile', 'kilometer')
        self.__metric = self.__us * 1.6
        self.output_metric_measures()

    # The fahrenheit_to_celsiu method one C = (F - 32) * 5/9
    def fahrenheit_to_celsiu(self):
        self.__us_name_plural = '';
        self.__metric_name_plural = '';
        self.__us = int(self.input_us_measures('Fahrenheit temperature', 'Celsiu temperature'))
        self.__metric = (self.__us - 32) * 5//9
        self.output_metric_measures()

    # The gallons_to_liters method one gallon to 3.9 liters
    def gallons_to_liters(self):
        self.input_us_measures('gallon', 'liter')
        self.__metric = self.__us * 3.9
        self.output_metric_measures()

    # The pounds_to_kilograms method one pound to 0.45 kilograms
    def pounds_to_kilograms(self):
        self.input_us_measures('pound', 'kilogram')
        self.__metric = self.__us * 0.45
        self.output_metric_measures()

    # The inches_to_centimeters method one inch to 2.54 centimeters
    def inches_to_centimeters(self):
        self.__us_name_plural = 'es';
        self.input_us_measures('inch', 'centimeter')
        self.__metric = self.__us * 2.54
        self.output_metric_measures()

# Global constants for menu choices
MILES = 1
FAHRENHEIT = 2
GALLONS = 3
POUNDS = 4
INCHES = 5
QUIT = 9

# The main function.
def main():
    convertor = Convertor()

    # Initialize a variable for the user's choice.
    choice = 0

    while choice != QUIT:
        choice = get_menu_choice()
        if choice == MILES:
            convertor.miles_to_kilometers()
        elif choice == FAHRENHEIT:
            convertor.fahrenheit_to_celsiu()
        elif choice == GALLONS:
            convertor.gallons_to_liters()
        elif choice == POUNDS:
            convertor.pounds_to_kilograms()
        elif choice == INCHES:
            convertor.inches_to_centimeters()
    else:
        print('------------------------------')
        print(' Bye! See you next time!')

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
    while count <= 0 or choice < MILES or choice > QUIT:
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
