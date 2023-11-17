from random import randint

'''
This function creates a list of random numbers of some specified length.

Parameter/Argument: an int
Returns: a list
'''
def generate_list(length):
    result = []
    for i in range(length):
        result.append(randint(1, 100))
    return result

# Generate 2 lists of random values
a = generate_list(20)
b = generate_list(25)

# Return a list that contains only common elements between the lists
# Use 1 line of code
result = set(a).intersection(set(b))
print(list(result))
