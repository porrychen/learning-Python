# Global Constant
MONTH_NAMES = ["January", "Febuary", "March", "April", "May", "June",
          "July", "August", "September", "October", "November",
          "December"]

# The main function.
def main():
    date = ''
    while date == '':
        date = input('Please enter a date(mm/dd/yy): ')
        show_date = format_date(date)
        if show_date != '':
            print(show_date)
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
                    date_list.append('%s %d, 20%s' % (MONTH_NAMES[int(date_list[0]) - 1], int(date_list[1]), date_list[2]))

                    correct = True
                else:
                    print('⭕ ERROR: The year(yy) must be two digits.')
            else:
                print('⭕ ERROR: The day(dd) must be an integer in the range 1 through 31.')
        else:
            print('⭕ ERROR: The month(mm) must be an integerin the range 1 through 12.')

    return date_list[-1] if correct else ''

# Call the main function.
main()
