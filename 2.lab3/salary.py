'''
    ====================================================
    -------------------- Begin Main --------------------
    ====================================================
'''
# Global constants

ERROR = "\n⭕  ERROR:"

# The main function.
def main():
    employee_name = input_employee_name(3)
    if employee_name != '':
        worked_hours = input_worked_hours(employee_name)

        if worked_hours != None:
            hour_pay = input_hour_pays(employee_name)

            if hour_pay != None:
                gross_salary = worked_hours * hour_pay
                print(employee_name, worked_hours, hour_pay, gross_salary)

    print('⬐-----------------------------⬎')
    print('             Bye! 🎃 ')
    print('⬑-----------------------------⬏')

# The input_employee_name function.
def input_employee_name(count, message = ''):
    if count == 0:
        print (ERROR, " must have an employee's name!")
        print()

        return ''
    else:
        if message != '':
            print()
            print(message)
        name = str(input("Please enter an employee's name: "))
        if name == '':
            message = "Did't enter an employee's name! " + (count == 2 and "☞ 🔥 This is last chance!" or "")
            return input_employee_name(count - 1, message)
        else :
            return name

# The input_worked_hours function.
def input_worked_hours(employee_name, less_value = 10):
    try:
        hours = float(input("Please enter " + employee_name + "'s hours worked: "))
        if hours < less_value:
            print(ERROR, 'hours worked must be large than or equal to', less_value)
            print()
        else:
            max_value = 31 * 24
            if hours > float(max_value):
                print(" 💭  " + employee_name + " hard work! (☞  ❤️  Up to", max_value, "hours a month)")
            return hours
    except ValueError:
        print(ERROR, 'hours worked must be valid numbers.')
        print()

# The input_hour_pays function.
def input_hour_pays(employee_name, less_value = 9):
    try:
        rate = float(input("Please enter an hourly pay rate for " + employee_name + ": "))
        if rate < less_value:
            print(ERROR, ' an hourly pay rate must be large than or equal to $', less_value, sep = '')
            print()
        else:
            return rate
    except ValueError:
        print(ERROR, 'an hourly pay rate must be valid numbers.')
        print()

def calculate_deduction(gross_salary):
    return 0


# Call the main function.
main()

'''
    ∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
    --------------------- End Main ---------------------
    ∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
'''
