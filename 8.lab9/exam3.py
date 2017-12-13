'''
Write a program that uses a main function to do the following. Your completed program will have 3 loops.
1. Use a loop that asks the user to enter a store’s sales amount for each day in a week (7 days). Use a good prompt message. Store the 7 sales amounts as float values in a list.

2. Next, write a second loop to calculate the total sales for the week. Display this total with an appropriate label.

3. Finally, create an output file called ‘sales.txt’. This will be a sequential text file. Write a third loop to write the sales for each day to the file, one value per line. Then write one more line to the file with the total sales. Do not write any labels to the file – just write the requested values. Be sure that you only write text to the file so that the file can be viewed using a program like NotePad.

4. Save the program file as firstName_lastName_exam3.py where you will substitute your own first and last name for firstName and lastName.

5. Attach the file to this test question. The question is set up to allow three attempts to attach the file within the same session. This is a precautionary setting in case something goes wrong in an attempt to attach the file.
'''
# Global constants
DAYS = 7

# The main function.
def main():
    sale_list = []
    
    # asks the user to enter a store’s sales amount for each day in a week (7 days)
    input_sale(sale_list)

    # calculate the total sales for the week
    total = total_sales(sale_list)

    # create an output file.
    write_sales(sale_list, total)

# The input_rainfall function.
def input_sale(sale_list):
    for day in range(DAYS):
        correct = False
        while not correct:
            try:
                # the user enter the rainfall in inches) for each of the 12 months and stores them in a list.
                sale = float(input('Please enter a store’s sales amount for each day in a week, now day' + str(day + 1) + ': '))
                sale_list.append(sale)

                correct = True
            except ValueError:
                print('⛔ ERROR: Must be a valid number of the store’s sales amount! \n')

# The total_sales function.
def total_sales(sale_list):
    total = 0
    
    for sale in sale_list:
        total += sale
        
    print('\nThe total sales for the week:', '$' + format(total, '.2f'))

    return total

# The write_sales function.
def write_sales(sale_list, total):
    # open a file
    sale_file = open('sales.txt', 'w')

    # write the sales for each day
    for sale in sale_list:
        sale_file.write(str(sale) + '\n')

    # write the total sales
    sale_file.write(str(total))

    # close the file
    sale_file.close()

# Call the main function.
main()
