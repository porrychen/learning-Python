# Program to convert Feet to miles

# declare global variable
MATINEE_PRICE = 8
REGULAR_PRICE = 9
DELUXE_PRICE  = 15

# The main function.
def main():
    # call ask_tickets function to get the number of each category
    matinee_tickets = ask_tickets('Matinee')
    print()
    regular_tickets = ask_tickets('Regular')
    print()
    deluxe_tickets = ask_tickets('Deluxe')

    # call calculate_revenue
    calculate_revenue(matinee_tickets, regular_tickets, deluxe_tickets)

    # display ending words
    print()
    print('⬐-----------------------------⬎')
    print('    Bye! See you next time!   ')
    print('⬑-----------------------------⬏')

# The ask_tickets function for asking users to enter a number.
def ask_tickets(categoryName, again = False):
    tickets = 0
    # asks how many tickets are sold for the category 
    try:
        if not again:
            print('How many ' + categoryName + '\'s tickets are sold?')
            
        tickets = int(input('Please ' + ('re-' if again else '') + 'enter a number: '))

        # validate the tickets
        if tickets < 0:
            print('\n⛔ ERROR: Number of ' + categoryName + '\'s tickets cannot be negative.', end = '\n\n')
            tickets = ask_tickets(categoryName, True)
            
    except ValueError:
        print('\n⛔ ERROR: Number of ' + categoryName + '\'s tickets must be valid numbers.', end = '\n\n')

        tickets = ask_tickets(categoryName, True)
    return tickets

# The calculate_revenue function for calculating total revenue.
def calculate_revenue(matineeTickets, regularTickets, deluxeTickets):
    total_revenue = matineeTickets * MATINEE_PRICE + \
                    regularTickets * REGULAR_PRICE + \
                    deluxeTickets * DELUXE_PRICE
    print('\nThe total revenue is', '$' + format(total_revenue, ',.2f'))

# Call the main function.
main()
