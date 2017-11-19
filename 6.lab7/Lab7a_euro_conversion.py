# Program to convert Euros to US Dollars, or vice versa
#    1 euro = 1.14 US dollars

def main():
    # Convert euros to dollars
    euros = float(input('Please input the number of euros: '))
    while euros < 0:
        print('Number of euros must be non-negative')
        euros = float(input('Please input the number of euros: '))
    eurosToDollars(euros)

    # Convert dollars to euros
    dollars = float(input('Please input the number of US dollars: '))
    while dollars < 0:
        print('Number of US dollars must be non-negative')
        dollars = float(input('Please input the number of US dollars: '))
    dollarsToEuros(dollars)

def eurosToDollars(euros):
    dollars = euros * 1.14
    print(format(euros, '.2f'),'euros is', format(dollars, '.2f'),'US dollars')
    print()

def dollarsToEuros(dollars):
    euros = dollars / 1.14
    print(format(dollars, '.2f'),'US dollars is', format(euros, '.2f'),'euros')
    print()
    
main()
