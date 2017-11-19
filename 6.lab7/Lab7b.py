# The main function.
def main():
    file_name = 'grades.txt'
    txt_file = open(file_name, 'w')

    for i in range(6):
        name = ''
        while name == '':
            name = get_name()

        grade = -1.0
        while grade < 0.0:
            grade = get_grade(name)

        txt_file.write(name + '\n')
        txt_file.write(str(grade) + '\n')

    txt_file.close()

    try:
        txt_file = open(file_name, 'r')

        for line in txt_file:
            print('', line, end = '')

        txt_file.close()
    except IOError as err:
        print('⭕', err)

    print('⬐------------------------------⬎')
    print(' ⭐  Bye! See you next time! ⭐ ')
    print('⬑------------------------------⬏')

def get_name():
    name = input('Please enter the student’s name: ')

    if name == '':
        print('The student’s name must not be an empty!')

    return name

def get_grade(name):
    try:
        grade = float(input('Please enter ' + name + '’s' + ' grade: '))
        if grade < 0 or grade > 100:
            print('⭕ ERROR: The grade must be in (0 ~ 100) ! \n')
            grade = -1.0

    except ValueError:
        print('⭕ ERROR: Must be a valid grade! \n')
        grade = -1.0

    return grade

# Call the main function.
main()
