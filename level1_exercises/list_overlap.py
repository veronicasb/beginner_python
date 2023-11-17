from random import randint

a = []
b = []
while len(a) < 25:
    a.append(randint(1, 100))
while len(b) < 36:
    b.append(randint(1, 100))

print([value for value in a if value in b])