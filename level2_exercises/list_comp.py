from random import randint

# Generate a random list

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

a = generate_list(20)


# Return a list of even elements from that list in 1 line of code

result = filter(lambda x: x % 2 == 0, a)
print(list(result))
# or
result = [x for x in a if x % 2 == 0]
print(result)