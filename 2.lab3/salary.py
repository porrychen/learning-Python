'''
    ====================================================
    -------------------- Begin Main --------------------
    ====================================================
'''
# Global constants

ERROR = "\n⭕  ERROR:"

# The main function.
def main():
    employee_salary()

    print('⬐-----------------------------⬎')
    print('             Bye! 🎃 ')
    print('⬑-----------------------------⬏')

def employee_salary(ask_again = True):
    employee_name = input_employee_name(3)
    if employee_name != '':
        worked_hours = input_worked_hours(employee_name)

        if worked_hours != None:
            hour_pay = input_hour_pays(employee_name)

            if hour_pay != None:
                gross_salary = worked_hours * hour_pay
                each_deduction = calculate_deductions(gross_salary)
                net_salary = gross_salary - each_deduction['deductions']

                print()
                print("The employee's name is ", employee_name, ".", sep = "")
                print(" ⦧ Gross salary: ", format_to_currency(gross_salary), \
                      " (hours worked is ", worked_hours, " and an hourly pay rate is ", format_to_currency(hour_pay), ")", sep = "")
                print(" ⦙ Deductions: ", format_to_currency(each_deduction['deductions']), sep = "\t")
                print(" ⦙   ⧁  Income tax: ", format_to_currency(each_deduction['tax_rate']), sep = "\t")
                print(" ⦙   ⧁  Social security tax: ", format_to_currency(each_deduction['social_security_rate']), sep = "\t")
                print(" ⦙   ⧁  Medical plan: ", format_to_currency(each_deduction['medical_rate']), sep = "\t")
                print(" ⦙   ⧁  Retirement.: ", format_to_currency(each_deduction['retirement_rate']), sep = "\t")
                print(" ⦦ Net salary: ", format_to_currency(net_salary), sep = "\t")

                if ask_again:
                    print()
                    again = str(input("Do you want to input another emplayee's salary? (y/n): ")).lower() == 'y'

                    if again:
                        print()
                        employee_salary()


# The format_to_currency function.
def format_to_currency(number):
    return '$' + format(number, ',.2f')

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

def calculate_deductions(gross_salary):
    result = {'tax_rate': 0, 'social_security_rate': 0,
              'medical_rate': 0, 'retirement_rate': 0,
              'deductions': 0}

    if gross_salary < 4000.0:
        result['tax_rate'] = gross_salary * 0.12
        result['social_security_rate'] = gross_salary * 0.04
        result['medical_rate'] = gross_salary * 0.01
    elif gross_salary < 8000.0:
        result['tax_rate'] = gross_salary * 0.2
        result['social_security_rate'] = gross_salary * 0.07
        result['medical_rate'] = gross_salary * 0.03
    elif gross_salary < 16000.0:
        result['tax_rate'] = gross_salary * 0.3
        result['social_security_rate'] = gross_salary * 0.09
        result['medical_rate'] = gross_salary * 0.05
    elif gross_salary >= 16000.0:
        result['tax_rate'] = gross_salary * 0.38
        result['social_security_rate'] = gross_salary * 0.11
        result['medical_rate'] = gross_salary * 0.07

    result['retirement_rate'] = gross_salary * 0.06

    result['deductions'] = result['tax_rate'] + result['social_security_rate'] + \
                        result['medical_rate'] + result['retirement_rate']

    return result


# Call the main function.
main()

'''
    ∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
    --------------------- End Main ---------------------
    ∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
'''
