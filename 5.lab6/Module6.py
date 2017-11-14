'''
    Write a program that does the following:

    Asks the user for the length and width of a rectangle.
    Asks the user for the side of a square.
    Asks the user for the radius of a circle.
    The program will then calculate and display the area of all three.
    Your program must be modular. It should have a main function that calls other functions to do most of the work. You must include the following functions in addition to main:

    A function, maybe called getRecLength, that will input and return the length of a rectangle.
    A function to input and return the width of a rectangle. This input will happen in a function.
    A function to input and return the side of a square.
     A function to input and return the radius of a circle.
    A function, maybe called displayRecArea, to calculate and print the area of a rectangle. The area of a rectangle is lenth time width.
    A function to calculate and display the area of a square. The area is side times side.
    A function to calculate and display the area of a circle. The area is pi times radius squared. Use 3.14 for pi.
'''
# The main function.
def main():
    # Asks the user for the length and width of a rectangle.
    length = getRecLength()
    width = getRecWidth()
    # Asks the user for the side of a square.
    side = getSquareSide()
    # Asks the user for the radius of a circle.
    radius = getCircleRadius()

    # The program will then calculate and display the area of all three.
    displayRecArea(length, width)
    displaySquareArea(side)
    displayCircleArea(radius)

# The getRecLength function will input and return the length of a rectangle.
def getRecLength():
    return float(input('Please enter the length of a rectangle: '))

# The getRecWidth function will input and return the width of a rectangle.
def getRecWidth():
    return float(input('Please enter the width of a rectangle: '))

# The getSquareSide function will input and return the side of a square.
def getSquareSide():
    return float(input('Please enter the side of a square: '))

# The getCircleRadius function will input and return the radius of a circle.
def getCircleRadius():
    return float(input('Please enter the radius of a circle: '))

# The displayRecArea function will calculate and print the area of a rectangle.
def displayRecArea(length, width):
    # The area of a rectangle is lenth time width.
    print('\nThe area of a rectangle is', length * width)

# The displaySquareArea function will calculate and display the area of a square.
def displaySquareArea(side):
    # The area is side times side.
    print('The area of a square is', side ** 2)

# The displayCircleArea function will calculate and display the area of a circle.
def displayCircleArea(radius):
    # Use 3.14 for pi.
    pi = 3.14
    # The area is pi times radius squared.
    print('The area of a circle is', pi * radius ** 2)

# Call the main function.
main()
