
try:
    number = int(input("Enter a number: "))
    print(number)
    break

# Best practice is to specify error when using "except"
except ValueError as err:
    print(err)
