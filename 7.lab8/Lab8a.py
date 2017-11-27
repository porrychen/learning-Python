# The main function.
def main():
    students = []
    getNames(students)
    displayList(students)

    students.sort()
    displayList(students)

    students.reverse()
    displayList(students)

    students.append('Bob Comer')
    students.insert(0, 'Porry Chen')

    writeFile(students)
    displayFile()

    students = tuple(students)
    displayList(students)

def getNames(nameList):
    print('=' * 11, '8 students\' name', '=' * 11)
    for i in range(8):
        nameList.append(input(str(i + 1) + '. Please enter a student\'s name: '))
    print('=' * 40)

def displayList(nameList):
    print()
    print(nameList)
    # for name in nameList:
    #     print(name)

def writeFile(nameList):
    nameFile = open('names.txt', 'w')

    for name in nameList:
        nameFile.write(name + '\n')

    nameFile.close()

def displayFile():
    nameFile = open('names.txt', 'r')

    print()
    for name in nameFile:
        print(name.rstrip())

    nameFile.close()

# Call the main function.
main()
