'''	
Write a program that does the following:

1.Store the following text into a string variable:  
The quick brown fox jumps over the lazy dog!  But then the lazy dog BITES the fox and then the fox SCREAMS at the lazy dog. Now YOU tell me who is at fault?

2.Write the appropriate code that determines the following about the characters in the string variable:
Number of upper case letters
Number of lower case letters
Number of spaces - count only the space characters (not whitespace characters)
Number of punctuation marks (include only period ('.'), comma (','), question mark ('?'), exclamation point ('!'), colon (':') and semicolon (';').
Length of the string

3.Copy the string into a new string and replace every occurrence of the word lazy with the word hyperactive.

4.Print all the values from step 2 above and print the original and changed strings.
'''
# The main function.
def main():
    # 1. Store the text into a string variable 'text'
    text = 'The quick brown fox jumps over the lazy dog!  But then the lazy dog BITES the fox and then the fox SCREAMS at the lazy dog. Now YOU tell me who is at fault?'

    # Initialize variable
    count_upper = 0
    count_lower = 0
    count_space = 0
    count_punctuation = 0

    # 2.
    for string in text:
        if string.isupper():
            # 2.1 Number of upper case letters
            count_upper += 1
        elif string.islower():
            # 2.2 Number of lower case letters
            count_lower += 1
        elif string == ' ':
            # 2.3 Number of spaces - count only the space characters (not whitespace characters)
            count_space += 1
        elif string in '.,?!:;':
            # 2.4 Number of punctuation marks (include only period ('.'), comma (','), question mark ('?'), exclamation point ('!'), colon (':') and semicolon (';').
            count_punctuation += 1

    # 2.5 Length of the string
    count_text = len(text)

    # 3. Copy the string into a new string
    new_text = text
    # replace every occurrence of the word lazy with the word hyperactive.
    new_text = new_text.replace('lazy', 'hyperactive')

    # 4. Print all the values from step 2 above and print the original and changed strings.
    print('\n------------- Report -------------')
    print('Number of upper case letters:', count_upper)
    print('Number of lower case letters:', count_lower)
    print(format('Number of spaces:', '29s'), count_space)
    print('Number of punctuation marks: ', count_punctuation)
    print(format('Length of the string:', '29s'), count_text)
    print('\nThe original string: "', text, '"', sep = '')
    print('The changed string: "', new_text, '"', sep = '')
    print('----------------------------------')


# Call the main function.
main()
