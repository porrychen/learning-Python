# The main function.
def main():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day = 1
    tatal_eggs = 0

    while day < 8:
        try:
            day_eggs = int(input('Please enter the number of eggs on ' + days[day - 1] + ': '))

            if day_eggs < 0:
                print("Error: must be a positive number!")
            else:
                tatal_eggs += day_eggs
                day += 1
        except ValueError:
            print ("Error: must be a valid number!")

    avg_eggs = tatal_eggs / 7

    print("\nHI, Brown!")
    print("The total number of eggs is", format(tatal_eggs, ","))
    print("The average number of eggs is", format(avg_eggs, ",.2f"))

    print()
    print('⬐-----------------------------⬎')
    print('    Bye! See you next time!    ')
    print('⬑-----------------------------⬏')

# Call the main function.
main()
