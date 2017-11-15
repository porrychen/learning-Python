import Lab6a_module as convert_module

# The main function.
def main():
    # Initialize a variable for the user's choice.
    choice = 0

    while choice != convert_module.QUIT:
        # choose one menu
        choice = convert_module.get_menu_choice()

        if choice in (convert_module.MILES, convert_module.FAHRENHEIT,
                      convert_module.GALLONS, convert_module.POUNDS,
                      convert_module.INCHES):

            # initialize variables for name, number, and what function will be called.
            name = ('', '')
            number = [0.0, 0.0]
            conversion = ''

            # print('Please tell me how many %(from_name)s you want converted to %(to_name)s quote types.' % {"from_name": "miles", "to_name": "555"})
            input_tips = 'Please tell me how many %s you want converted to %s.'
            input_message = 'Enter a number: '
            output_message = ' %f %s is equal to %f %s ';

            # one by one to check what the user selects, then run statement correctly
            if choice == convert_module.MILES:
                name = ('miles', 'kilometers')
                conversion = 'convert_module.milesToKm(%f)'

                #number[1] = convert_module.milesToKm(number[0])
            elif choice == convert_module.FAHRENHEIT:
                name = ('F temperature', 'C temperature')
                conversion = 'convert_module.degreesFToC(%f)'
                #number[1] = convert_module.degreesFToC(number[0])
            elif choice == convert_module.GALLONS:
                name = ('gallons', 'liters')
                conversion = 'convert_module.gallonsToLiters(%f)'
                #number[1] = convert_module.gallonsToLiters(number[0])
            elif choice == convert_module.POUNDS:
                name = ('pounds', 'kilograms')
                conversion = 'convert_module.poundsToKg(%f)'
                #number[1] = convert_module.poundsToKg(number[0])
            elif choice == convert_module.INCHES:
                name = ('inches', 'centimeters')
                conversion = 'convert_module.poundsToKg(%f)'
                #number[1] = convert_module.inchesToCm(number[0])

            # do all the input
            print(input_tips % name)
            number[0] = float(input(input_message))
            # call the conversion functions in the module to do the calculations
            number[1] = eval(conversion % (number[0]))

            # display and format converted result
            output_message = output_message % (number[0], name[0], number[1], name[1])
            len_output_message = len(output_message)
            print('↓' * len_output_message, output_message, '↑' * len_output_message, sep = '\n')
    else:
        print('------------------------------')
        print(' Bye! See you next time!')

# Call the main function.
main()
