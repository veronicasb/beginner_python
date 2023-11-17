from random import sample

# Generate 2 lists of random values
a = sample(range(100), 20)
b = sample(range(100), 25)

# Return a list that contains only common elements between the lists (no duplicates)
# Use at least 1 list comprehension
result = set([x for x in a if x in b])
print(list(result))