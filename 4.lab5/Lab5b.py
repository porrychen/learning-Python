# Program to convert Feet to miles

# declare global variable
MATINEE_PRICE = 8
REGULAR_PRICE = 9
DELUXE_PRICE  = 15

# The main function.
def main():
    category_names = ['Matinee', 'Regular', 'Deluxe']
    category_tickets = [0, 0, 0]
    count = 0
    again = False

    # loop for getting the number of each category
    while count < len(category_names):
        tickets = 0
        # asks how many tickets are sold for the category
        try:
            if not again:
                print('How many ' + category_names[count] + '\'s tickets are sold?')

            tickets = int(input('Please ' + ('re-' if again else '') + 'enter a number: '))

            # validate the tickets
            if tickets < 0:
                print('\n⛔ ERROR: Number of ' + category_names[count] + '\'s tickets cannot be negative.', end = '\n\n')
                again = True
            else:
                category_tickets[count] = tickets

                again = False
                count += 1
                print()
        except ValueError:
            print('\n⛔ ERROR: Number of ' + category_names[count] + '\'s tickets must be valid numbers.', end = '\n\n')

            again = True

    # call calculate_revenue
    calculate_revenue(category_tickets[0], category_tickets[1], category_tickets[2])

    # display ending words
    print()
    print('⬐-----------------------------⬎')
    print('    Bye! See you next time!   ')
    print('⬑-----------------------------⬏')

# The calculate_revenue function for calculating total revenue.
def calculate_revenue(matineeTickets, regularTickets, deluxeTickets):
    total_revenue = matineeTickets * MATINEE_PRICE + \
                    regularTickets * REGULAR_PRICE + \
                    deluxeTickets * DELUXE_PRICE
    print('\nThe total revenue is', '$' + format(total_revenue, ',.2f'))

# Call the main function.
main()
