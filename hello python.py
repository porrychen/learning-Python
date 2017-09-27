# This is my first python file
year = 2017
month = 9
day = 27

# How many classmates
students = 10
attdents = int(input("How many students attdent?"))

# How many absent
absent = students - attdents

# If everyone needs to pay $3
pay = 3

# Today total money
total = attdents * pay

if attdents > 3:
    # show absent
    print("Absent is ", absent)
else:
    print(input("Are you here?")) 

# show total
print("you get total money are $", total, " on ", month, "/", day, "/", year)
