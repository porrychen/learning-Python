# This program allows the user to input
# an employee's salary for SoftwarePirates Inc.

'''
    ===================================================
    ------------------- Begin Class -------------------
    ===================================================
'''
# the Employee class is an employee's name and monthly salary.
class Employee(object):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def gross_salary(self):
        return self._gross_salary

    @property
    def each_deduction(self):
        return self._each_deduction

    @property
    def net_salary(self):
        return self._net_salary

    def new_salary(self):
        result = False

        self._worked_hours = self._input_worked_hours()
        if self._worked_hours != None:
            self._hour_pays_rate = self._input_hour_pays()

            if self._hour_pays_rate != None:
                self._calculate_salary()
                result = True

        return result

    def display_salary(self, count = 0):
        print()
        if count > 0:
            print(count, '.', sep = '', end = '')
        print("The employee's name is ", self.name, ".", sep = "")
        print(" ⦧ Gross salary: ", format_to_currency(self.gross_salary), \
              " (hours worked is ", self._worked_hours, " and an hourly pay rate is ", format_to_currency(self._hour_pays_rate), ")", sep = "")
        print(" ⦙ Deductions: ", format_to_currency(self.each_deduction['deductions']), sep = "\t")
        print(" ⦙   ⧁  Income tax: ", format_to_currency(self.each_deduction['tax_rate']), sep = "\t")
        print(" ⦙   ⧁  Social security tax: ", format_to_currency(self.each_deduction['social_security_rate']), sep = "\t")
        print(" ⦙   ⧁  Medical plan: ", format_to_currency(self.each_deduction['medical_rate']), sep = "\t")
        print(" ⦙   ⧁  Retirement.: ", format_to_currency(self.each_deduction['retirement_rate']), sep = "\t")
        print(" ⦦ Net salary: ", format_to_currency(self.net_salary), sep = "\t")

    # The input_worked_hours method.
    def _input_worked_hours(self, again = True, less_value = 10):
        try:
            self._worked_hours = float(input("Please enter " + self.name + "'s hours worked: "))
            if self._worked_hours < less_value:
                print(ERROR, 'hours worked must be large than or equal to', less_value)
                print()
            else:
                max_value = 31 * 24
                if self._worked_hours > float(max_value):
                    print(" 💭  " + self.name + " hard work! (☞  ❤️  Up to", max_value, "hours a month)")
                return self._worked_hours
        except ValueError:
            print(ERROR, 'hours worked must be valid numbers.')
            print()

        if again:
            done = str(input("Do you want to enter " + self.name + "'s hours worked, again? (Y/n): ")).lower() == 'n'
            if not done:
                return self._input_worked_hours(False)

    # The input_hour_pays method.
    def _input_hour_pays(self, again = True, less_value = 9):
        try:
            self._hour_pays_rate = float(input("Please enter an hourly pay rate for " + self.name + ": "))
            if self._hour_pays_rate < less_value:
                print(ERROR, ' an hourly pay rate must be large than or equal to ', format_to_currency(less_value), sep = '')
                print()
            else:
                return self._hour_pays_rate
        except ValueError:
            print(ERROR, 'an hourly pay rate must be valid numbers.')
            print()

        if again:
            done = str(input("Do you want to enter an hourly pay rate for " + self.name + ", again? (Y/n): ")).lower() == 'n'
            if not done:
                return self._input_hour_pays(False)

    # This calculate_salary method.
    def _calculate_salary(self):
        self._gross_salary = self._worked_hours * self._hour_pays_rate
        self._calculate_deductions(self._gross_salary)
        self._net_salary = self._gross_salary - self._each_deduction['deductions']

    # This calculate_deductions method.
    def _calculate_deductions(self, gross_salary):
        self._each_deduction = {'tax_rate': 0, 'social_security_rate': 0,
                  'medical_rate': 0, 'retirement_rate': 0,
                  'deductions': 0}

        if gross_salary < 4000.0:
            self._each_deduction['tax_rate'] = gross_salary * 0.12
            self._each_deduction['social_security_rate'] = gross_salary * 0.04
            self._each_deduction['medical_rate'] = gross_salary * 0.01
        elif gross_salary < 8000.0:
            self._each_deduction['tax_rate'] = gross_salary * 0.2
            self._each_deduction['social_security_rate'] = gross_salary * 0.07
            self._each_deduction['medical_rate'] = gross_salary * 0.03
        elif gross_salary < 16000.0:
            self._each_deduction['tax_rate'] = gross_salary * 0.3
            self._each_deduction['social_security_rate'] = gross_salary * 0.09
            self._each_deduction['medical_rate'] = gross_salary * 0.05
        elif gross_salary >= 16000.0:
            self._each_deduction['tax_rate'] = gross_salary * 0.38
            self._each_deduction['social_security_rate'] = gross_salary * 0.11
            self._each_deduction['medical_rate'] = gross_salary * 0.07

        self._each_deduction['retirement_rate'] = gross_salary * 0.06

        self._each_deduction['deductions'] = self._each_deduction['tax_rate'] + self._each_deduction['social_security_rate'] + \
                            self._each_deduction['medical_rate'] + self._each_deduction['retirement_rate']

'''
    -------------------- End Class --------------------
    ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
'''

# Global constants

ERROR = "\n⭕  ERROR:"

# The format_to_currency function.
def format_to_currency(number):
    return '$' + format(number, ',.2f')

'''
    ====================================================
    -------------------- Begin Main --------------------
    ====================================================
'''
# The main function.
def main():
    total_salaries = 0.0
    employees_count = {"error": 0, "total": 0}

    employee_name = input_employee_name()
    while employee_name != '':
        employee = Employee(employee_name)
        if employee.new_salary():
            employee.display_salary(employees_count['total'] + 1)

            total_salaries += employee.gross_salary
        else:
            employees_count['error'] += 1

        employees_count['total'] += 1

        del employee
        employee_name = input_employee_name()

    if employees_count['total'] > 0:
        print()
        print("⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅")
        print("  The number of employees is ", employees_count['total'], " (including ", employees_count['error'], " error", ("s" if employees_count['error'] > 1 else ""), ")", sep = "")
        print("  The total of the base salaries for all employees is ", format_to_currency(total_salaries))
        print("⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅")
        print()

    print('⬐-----------------------------⬎')
    print('             Bye! 🌱 ')
    print('⬑-----------------------------⬏')

# The input_employee_name function.
def input_employee_name():
    print()
    name = str(input("Please enter an employee's name (an 'empty' name will STOP this input❗ ): "))

    while name == '':
        continued = str(input("⚠️  Did't enter an employee's name! ☞  Want to QUIT? (Y/n): ")).lower() == 'n'
        if continued:
            print()
            name = str(input("Please re-enter an employee's name (an 'empty' name will STOP this input❗ ): "))
        else:
            name = 'empty'

    if name == 'empty':
        return ''
    else:
        return name

# Call the main function.
main()

'''
    ∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
    --------------------- End Main ---------------------
    ∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
'''
