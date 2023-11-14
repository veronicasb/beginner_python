# Ask user for input
number = ""
while number == "":
    try:
        number = int(input("\nEnter a number: "))
    except ValueError:
        print("\nPlease enter a number...")

# Let the user now if the number is even or odd
check = number % 2
if check == 0:
    print("\nThe number you entered is an even number!")
else:
    print("\nThe number you entered is an odd number!")

# If it's a multiple of 4, print another message
check_multiple_of_4 = number % 4
if check_multiple_of_4 == 0:
    print("\nThe number you entered is also a multiple of 4!")
else:
    print("\nThe number you entered is not a multiple of 4!")

# Ask user for another number
divide_by = ""
while divide_by == "":
    try:
        divide_by = int(input("\nEnter a number: "))
    except ValueError:
        print("\nPlease enter a number...")

# If number divides evenly into first number, print another message
check_multiple_of_num = number % divide_by
if check_multiple_of_num == 0:
    print("\nThe number you entered divides evenly by " + str(divide_by) + "!")
else:
    print("\nThe number you entered does not divide evenly by " + str(divide_by) + "!")
