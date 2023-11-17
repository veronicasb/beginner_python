# List methods update list itself
signs = [888, 333, 444, 111, 666]
friends = ["Valorie", "Alexia", "Cindy"]
friends.pop()
friends.extend(signs)
friends.append("Cindy")
print(friends)
friends.insert(2, "who")
print(friends)
print(friends[friends.index("Cindy")])
print(friends.count("Valorie"))
signs.sort()
print(signs)
signs.reverse()
print(signs)
signs_copy = signs.copy()
print(signs_copy)

# Tuples - container that stores 2 values
# Tuples are immutable (they cant be changed or modified)
coordinates = (-0.1234213, )

