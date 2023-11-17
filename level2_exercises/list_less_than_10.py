from functools import reduce

# Take a list
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Request a comparison value
num = int(input("Enter a number: "))

# Print out all elements that are less than 5
result = filter(lambda x: x < num, a)
print(list(result))
# or
result = [x for x in a if x < num]
print(result)