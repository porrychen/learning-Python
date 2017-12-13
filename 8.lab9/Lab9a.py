# The main function.
def main():
    done = False

    while not done:
        email_address = ''

        while email_address == '':
            # 1. input the email address in a validation loop
            email_address = input('Please enter a student\'s email address(firstname.lastname@g.austincc.edu): ')

            # 2. validate the address
            if not check_email(email_address):
                email_address = ''
            else:
                # 3. extract the student’s first name and last name from the email address
                name_list = extract_email(email_address)
                # 4. display the student’s name
                show_name(name_list)

        # ask the user whether try again
        done = input('\nDo you want to enter a new student\'s email address? (Y/n)').lower() == 'n'

    print('⬐-----------------------------------⬎')
    print(' ⭐  Thank you for using this app! ⭐ ')
    print(' ⭐  Bye! See you next time!       ⭐ ')
    print('⬑-----------------------------------⬏')

# The check_email function.
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
        elif period_index == 0:
            print('⭕ ERROR: Must have a first or last name!')
        elif sign_index < 0:
            print('⭕ ERROR: Must be a @ sign in an email address!')
        else:
            print('⭕ ERROR: Must be a correct email address!')
        print('(The format of the email address is firstname.lastname@g.austincc.edu)')
        print()

    return result

# The extract_email function.
def extract_email(email):
    # extract the student’s first name and last name from the email address
    name_list = email.split('@')[0].split('.')
    
    if len(name_list[0]) > 0:
        # capitalize the first letter of firstname
        name_list[0] = name_list[0][0].upper() + (name_list[0][1:] if len(name_list[0]) > 1 else '')
    if len(name_list) > 1 and len(name_list[-1]) > 0:
        # capitalize the first letter of lastname
        name_list[-1] = name_list[-1][0].upper() + (name_list[-1][1:] if len(name_list[-1]) > 1 else '')
    else:
        name_list.append('')

    return name_list

# The show_name function.
def show_name(name_list):
    name = '%s %s' % (name_list[0], name_list[-1])

    # display the student’s name
    print('The student’s name:', name.strip())
    
# Call the main function.
main()
