import calendar

# Global Constant
MONTH_NAMES = ["January", "Febuary", "March", "April", "May", "June",
          "July", "August", "September", "October", "November",
          "December"]

# The main function.
def main():
    # initialize a flag 
    done = False

    # if not done, then continue
    while not done:
        date = ''
        while date == '':
            # 1. input a date in numeric format
            date = input('Please enter a date(mm/dd/yy): ')

            # 2. check the date is valid
            date = check_date(date)
            
            if date != '':
                # 3.output the date in long date format
                show_date(date)

        # ask the user whether try again
        done = input('\nDo you want to enter a new date? (Y/n)').lower() == 'n'

    print('⬐-----------------------------------⬎')
    print(' ⭐  Thank you for using this app! ⭐ ')
    print(' ⭐  Bye! See you next time!       ⭐ ')
    print('⬑-----------------------------------⬏')

# The check_date function.
def check_date(date):
    correct = False

    date_list = date.split('/')

    if len(date_list) == 3:
        if date_list[0].isdigit() and int(date_list[0]) in range(1, 13):
            if date_list[1].isdigit() and int(date_list[1]) in range(1, 32):
                if date_list[2].isdigit() and len(date_list[2]) == 2:
                    correct = True
                else:
                    print('⭕ ERROR: The year(yy) must be two digits.')
            else:
                print('⭕ ERROR: The day(dd) must be an integer in the range 1 through 31.')
        else:
            print('⭕ ERROR: The month(mm) must be an integer in the range 1 through 12.')
    elif date != '':
        print('⭕ ERROR: Must be a correct format of a date!')
    
    return date if correct else ''

# The show_date function.
def show_date(date):
    date_list = date.split('/')

    date_list[2] = int(date_list[2]) + 2000
    # output the date in long date format
    print('\n%s %d, %s' % (MONTH_NAMES[int(date_list[0]) - 1], int(date_list[1]), date_list[2]))

    # use calendar module to further check
    # first day of the month and number of days in month
    month_range = calendar.monthrange(date_list[2], int(date_list[0]))
    if int(date_list[1]) > month_range[1]:
        print('Actually, the max day is ' + str(month_range[1]))

# Call the main function.
main()
