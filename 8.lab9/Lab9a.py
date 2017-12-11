# The main function.
def main():
    email_address = ''

    while email_address == '':
        # input the email address in a validation loop
        email_address = input('Please enter a student\'s email address(firstname.lastname@g.austincc.edu): ')

        # validate the address
        if not check_email(email_address):
            email_address = ''
        else:
            name_list = email_address.split('@')[0].split('.')
            # firstname
            name_list[0] = name_list[0][0].upper() + name_list[0][1:]
            # lastname
            name_list[-1] = name_list[-1][0].upper() + name_list[-1][1:]

            print('The student’s name is', name_list[0], name_list[-1])

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
        print('⭕ ERROR: Must be a correct email address!')
        print('(The format of the email address is firstname.lastname@g.austincc.edu)')

    return result

# Call the main function.
main()
