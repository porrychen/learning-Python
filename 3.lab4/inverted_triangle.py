# This program draw an inverted triangle using nested loops.

'''
    ====================================================
    -------------------- Begin Main --------------------
    ====================================================
'''
# The main function.
def main():
    # initialize variables
    loops_count = 10

    # when loops_count is greater than 0
    while loops_count > 0:
        rows_asterisks = ''
        for i in range(0, loops_count):
            rows_asterisks += '*'
        print(rows_asterisks)
        loops_count -= 1

# Call the main function.
main()

'''
    ∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
    --------------------- End Main ---------------------
    ∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
'''
