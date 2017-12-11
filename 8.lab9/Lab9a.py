# The main function.
def main():
    done = False

    while not done:
        email_address = ''

        while email_address == '':
            # input the email address in a validation loop
            email_address = input('Please enter a student\'s email address(firstname.lastname@g.austincc.edu): ')

            # validate the address
            if not check_email(email_address):
                email_address = ''
            else:
                # extract the student’s first name and last name from the email address
                name_list = email_address.split('@')[0].split('.')
                if len(name_list[0]) > 0:
                    # capitalize the first letter of firstname
                    name_list[0] = name_list[0][0].upper() + (name_list[0][1:] if len(name_list[0]) > 1 else '')
                if len(name_list) > 1 and len(name_list[-1]) > 0:
                    # capitalize the first letter of lastname
                    name_list[-1] = name_list[-1][0].upper() + (name_list[-1][1:] if len(name_list[-1]) > 1 else '')
                else:
                    name_list.append(' ')
                # display the student’s name
                print('The student’s name is', name_list[0], name_list[-1])

        # ask the user whether try again
        done = input('Do you want to enter a new strent\'s email address? (Y/n)').lower() == 'n'

    print('⬐-----------------------------------⬎')
    print(' ⭐  Thank you for using this app! ⭐ ')
    print(' ⭐  Bye! See you next time!       ⭐ ')
    print('⬑-----------------------------------⬏')

def check_email(email):
    result = False

    # search for the position of the first period
    period_index = email.find('.')
    # search for the position of the @ sign
    sign_index = email.find('@')

    # contains both a period and an @ sign, all alphabetic characters are lower case
    if period_index > -1 and sign_index > -1 and period_index < sign_index and email.islower():
            result = True
    elif email != '':
        if period_index < 0:
            print('⭕ ERROR: Use a period sign to separate the first and last names!')
        elif sign_index < 0:
            print('⭕ ERROR: Must be a @ sign in an email address!')
        else:
            print('⭕ ERROR: Must be a correct email address!')
        print('(The format of the email address is firstname.lastname@g.austincc.edu)')
        print()

    return result

# Call the main function.
main()
