import calendar

# Global Constant
MONTH_NAMES = ["January", "Febuary", "March", "April", "May", "June",
          "July", "August", "September", "October", "November",
          "December"]

# The main function.
def main():
    done = False

    while not done:
        date = ''
        while date == '':
            date = input('Please enter a date(mm/dd/yy): ')
            show_date = format_date(date)
            if show_date != '':
                # output the date in long date format
                print(show_date)
            else:
                date = ''

        # ask the user whether try again
        done = input('\nDo you want to enter a new date? (Y/n)').lower() == 'n'

    print('⬐-----------------------------------⬎')
    print(' ⭐  Thank you for using this app! ⭐ ')
    print(' ⭐  Bye! See you next time!       ⭐ ')
    print('⬑-----------------------------------⬏')

def format_date(date):
    correct = False

    date_list = date.split('/')

    if len(date_list) == 3:
        if date_list[0].isdigit() and int(date_list[0]) in range(1, 13):
            if date_list[1].isdigit() and int(date_list[1]) in range(1, 32):
                if date_list[2].isdigit() and len(date_list[2]) == 2:
                    date_list[2] = int(date_list[2]) + 2000
                    date_list.append('%s %d, %s' % (MONTH_NAMES[int(date_list[0]) - 1], int(date_list[1]), date_list[2]))

                    # use calendar module to further check
                    # first day of the month and number of days in month
                    month_range = calendar.monthrange(date_list[2], int(date_list[0]))
                    if int(date_list[1]) > month_range[1]:
                        date_list[-1] += '\nActually, the max day is ' + str(month_range[1])

                    correct = True
                else:
                    print('⭕ ERROR: The year(yy) must be two digits.')
            else:
                print('⭕ ERROR: The day(dd) must be an integer in the range 1 through 31.')
        else:
            print('⭕ ERROR: The month(mm) must be an integer in the range 1 through 12.')
    elif date != '':
        print('⭕ ERROR: Must be a correct format of a date!')

    return date_list[-1] if correct else ''

# Call the main function.
main()
