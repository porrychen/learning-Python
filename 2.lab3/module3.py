# The main function.
def main():
    rectangle_length = float(input('Please enter a rectangle length: '))
    rectangle_width = float(input('Please enter a rectangle width: '))
    rectangle_area = rectangle_length * rectangle_width

    square_side = float(input('Please enter a square side: '))
    square_area = square_side ** 2

    print("\nThe area of the rectangle is", rectangle_area)
    print("The area of the square is", square_area)

    print()
    if rectangle_area > square_area:
        print("The rectangle has the largest area!")
    elif rectangle_area < square_area:
        print("The square has the largest area!")
    else:
        print("The area of the rectangle is equal to the area of the square!")

    print()
    print('⬐-----------------------------⬎')
    print('    Bye! See you next time!    ')
    print('⬑-----------------------------⬏')

# Call the main function.
main()
