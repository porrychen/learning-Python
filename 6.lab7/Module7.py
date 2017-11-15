'''
    Create a simple text file. You can use a text editor like NotePad, or you can also use the Python IDLE editor if you change the file type to .txt when you save the file. In the file store the integers 1 through 10. Put one number per line, and press the enter key after each number to end the line with a newline character. Save this file as firstnameLastnameNumbers.txt where you will replace firstNameLastname with your actual first and last name.

    Now write a program that does the following:

    Open the numbers.txt file, read the numbers and write them to another file called firstNamelastNameOutFile.txt. By now you know what to do with firstnamelastName!
    Then append the numbers 11 through 20 to OutFile.txt.
    Include a try/except statement in your program. The exception handler should print an appropriate error message and end the program if you are unable to open any of the files.
    Save your file as firstName_LastName_Module7.py where you will replace  firstName_LastName with your actual first and last name. Attach the file here just like you attach assignments.
'''
# The main function.
def main():
    try:
        # Open the numbers.txt file, read the numbers
        in_file = open('Numbers.txt', 'r')
        # Open another file, if use 'a', it will append again
        out_file = open('OutFile.txt', 'w')

        # write numbers.txt to the out file
        for line in in_file:
            out_file.write(line)

        # append the numbers 11 through 20 to OutFile.txt.
        for i in range(11, 21):
            out_file.write(str(i) + '\n')

        # close these files
        in_file.close()
        out_file.close()
    except IOError as err:
        # print an appropriate error message and end the program.
        print('⛔', err)
        print()

# Call the main function.
main()
