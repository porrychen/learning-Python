# This program allows the user to choose various
# conversions from a menu.

'''
    ===================================================
    ------------------- Begin Class -------------------
    ===================================================
'''
# the Convertor class is a parent class.
class Convertor():
    def __init__(self, from_number = None):
        self._from_number = from_number
        self._to_number = 0.0

    @property
    def from_name(self):
        return self._from_name

    @property
    def from_number(self):
        return self._from_number

    @property
    def to_name(self):
        return self._to_name
    
    @property
    def to_number(self):
        return self._to_number

    @property
    def is_allow_negative_number(self):
        return False

    @property
    def max_from_number(self):
        return -1

    def is_single_number(self, number):
        return (number != None) and (number == 0.0 or number == 1.0)

    def verify_number(self, number):
        result = self.is_allow_negative_number

        if not result:
            if number < 0.0:
                print('ERROR: must be not a negative number.')
                print()
            else:
                result = True

        if result and self.max_from_number > 0:
            if self.from_number > self.max_from_number:
                print('ERROR: must be lower than or equal to ', self.max_from_number, ' number.', sep = '')
                print()
                result = False
        
        return result

    # The input_number method enter a number for convertor
    def input_number(self):
        print('Please tell me how many ', self.from_name, ' you want converted to ', self.to_name, sep = '')
        try:
            self._from_number = float(input('Enter a number: '))
            return self.verify_number(self._from_number)
        except ValueError:
            print('ERROR: must be a valid number.')
            print()

    # The output_result method displays result
    def output_result(self):
        result = ' ' + str(self.from_number) + ' ' + self.from_name + \
                 ' is equal to ' + \
                 format(self.to_number, ',.5f') + ' ' + self.to_name + ' '
        pix_result = ''
        siff_result = ''
        for i in range(0, len(result)):
            pix_result += '↓'
            siff_result += '↑'

        print(pix_result, result, siff_result, sep = '\n')

        self._from_number = None
        self._to_number = 0.0

    # The convertor method convert from_number to result number
    def convertor(self):
        if self.from_number == None or not self.verify_number(self._from_number):
            if self.input_number():
                self.output_result()
        else:
            self.output_result()

# The Miles convert miles_to_kilometers.
# one mile to 1.6 kilometers
# It is a subclass of the Convertor class.
class Miles(Convertor):
    @Convertor.from_name.getter
    def from_name(self):
        return self.is_single_number(self.from_number) and 'mile' or 'miles'

    @Convertor.to_name.getter
    def to_name(self):
        return self.is_single_number(self.to_number) and 'kilometer' or 'kilometers'

    @Convertor.to_number.getter
    def to_number(self):
        return None if self.from_number == None else self.from_number * 1.6 

# The Fahrenheit convert F temperature to C.
# C = (F - 32) * 5/9
# It is a subclass of the Convertor class.
class Fahrenheit(Convertor):
    @Convertor.from_name.getter
    def from_name(self):
        return 'Fahrenheit temperature'

    @Convertor.to_name.getter
    def to_name(self):
        return 'Celsius temperature'

    @Convertor.is_allow_negative_number.getter
    def is_allow_negative_number(self):
        return True

    @Convertor.max_from_number.getter
    def max_from_number(self):
        return 1000

    @Convertor.to_number.getter
    def to_number(self):
        return None if self.from_number == None else (self.from_number  - 32) * 5 / 9 

# The Gallons convert gallons_to_liters.
# one gallon to 3.9 liters
# It is a subclass of the Convertor class.
class Gallons(Convertor):
    @Convertor.from_name.getter
    def from_name(self):
        return self.is_single_number(self.from_number) and 'gallon' or 'gallons'

    @Convertor.to_name.getter
    def to_name(self):
        return self.is_single_number(self.to_number) and 'liter' or 'liters'

    @Convertor.to_number.getter
    def to_number(self):
        return None if self.from_number == None else self.from_number * 3.9 

# The Pounds convert pounds_to_kilograms
# one pound to 0.45 kilograms.
# It is a subclass of the Convertor class.
class Pounds(Convertor):
    @Convertor.from_name.getter
    def from_name(self):
        return self.is_single_number(self.from_number) and 'pound' or 'pounds'

    @Convertor.to_name.getter
    def to_name(self):
        return self.is_single_number(self.to_number) and 'kilogram' or 'kilograms'

    @Convertor.to_number.getter
    def to_number(self):
        return None if self.from_number == None else self.from_number * 0.45 

# The Inches convert inches_to_centimeters
# one inch to 2.54 centimeters.
# It is a subclass of the Convertor class.
class Inches(Convertor):
    @Convertor.from_name.getter
    def from_name(self):
        return self.is_single_number(self.from_number) and 'inch' or 'inches'

    @Convertor.to_name.getter
    def to_name(self):
        return self.is_single_number(self.to_number) and 'centimeter' or 'centimeters'

    @Convertor.to_number.getter
    def to_number(self):
        return None if self.from_number == None else self.from_number * 2.54
    
'''
    -------------------- End Class --------------------
    ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
'''

'''
    ====================================================
    -------------------- Begin Main --------------------
    ====================================================
'''

# Global constants for menu choices
MILES = 1
FAHRENHEIT = 2
GALLONS = 3
POUNDS = 4
INCHES = 5
QUIT = 9

# The main function.
def main():
    # Initialize a variable for the user's choice.
    choice = 0

    while choice != QUIT:
        choice = get_menu_choice()
        if choice == MILES:
            convertor = Miles()
        elif choice == FAHRENHEIT:
            convertor = Fahrenheit()
        elif choice == GALLONS:
            convertor = Gallons()
        elif choice == POUNDS:
            convertor = Pounds()
        elif choice == INCHES:
            convertor = Inches()

        if isinstance(convertor, Convertor):
            convertor.convertor()

            del convertor
    else:
        print('------------------------------')
        print(' Bye! See you next time!')

# The get_menu_choice function displays the menu
# and gets a validated choice from the user.
def get_menu_choice():
    count = 0
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

# Call the main function.
main()

'''
    ====================================================
    --------------------- End Main ---------------------
    ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
'''
