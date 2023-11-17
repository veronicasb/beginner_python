from functools import reduce

# Take a list
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Request a comparison value
num = ""
while not num:
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Please enter a number...\n")

# Print out all elements that are less than some number
result = filter(lambda x: x < num, a)
print(list(result))
# or
result = [x for x in a if x < num]
print(result)