# The main function.
def main():
    # create an empty list
    students = []
    # input 8 student names rom the keyboard
    getNames(students)
    # display the contents of the list of students
    displayList(students)

    # sort the list in alphabetical order
    students.sort()
    # display to verify that the list was correctly sorted
    displayList(students)

    # reverse the order of the list contents
    students.reverse()
    # display to verify that the list was correctly reversed
    displayList(students)

    # append my professor’s name to the end of the list
    students.append('Bob Comer')
    # insert my own name at the beginning of the list
    students.insert(0, 'Porry Chen')

    # write the list to a file
    writeFile(students)
    # display the contents of the file
    displayFile()

    # convert the list to a Tuple
    students = tuple(students)
    # display to verify that the contents of the tuple is correct
    displayList(students)

# The getNames function.
def getNames(nameList):
    print('=' * 11, '8 students\' name', '=' * 11)
    for i in range(8):
        nameList.append(input(str(i + 1) + '. Please enter a student\'s name: '))
    print('=' * 40)

# The displayList function.
def displayList(nameList):
    print()
    print(nameList)
    # for name in nameList:
    #     print(name)

# The writeFile function.
def writeFile(nameList):
    nameFile = open('names.txt', 'w')

    for name in nameList:
        nameFile.write(name + '\n')

    nameFile.close()

# The displayFile function.
def displayFile():
    nameFile = open('names.txt', 'r')

    print()
    for name in nameFile:
        print(name.rstrip())

    nameFile.close()

# Call the main function.
main()
