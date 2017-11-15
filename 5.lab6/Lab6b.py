import random

# The main function.
def main():
    # Initialize a variable for running again.
    done = False

    while not done:
        # Generate a random number between 1 and 100. 
        random_num = random.randint(1, 100)

        # Initialize variables
        count = 0
        corrected = False

        # loop the player's input, if not correct
        while not corrected:
            try:
                # Ask the player to guess the number. 
                guess_num = int(input('Please enter a number you guess: '))
                # Keep track of the number of guesses.
                count += 1
                
                if guess_num < 1 or guess_num > 100:
                    print('The number between 1 and 100. ಠ_ಠ\n')
                elif guess_num > random_num:
                    # If the player’s guess is larger than the generated number
                    print('Too high!')
                elif guess_num < random_num:
                    # If the player’s guess is samller than the actual number
                    print('Too low!')
                else:
                    # The player guesses the number
                    corrected = True
                    print('\nYes, good job ♥‿♥! You guessed the number in %d tries!' % (count))
                    print()
            except ValueError:
                print('⛔ ERROR: Must be a valid number.\n')

        # Ask players if they wish to play again
        done = input('\nDo you want to guess another number? (Y/n): ').lower() == 'n'

    print('------------------------------')
    print(' Bye! See you next time!')

# Call the main function.
main()
