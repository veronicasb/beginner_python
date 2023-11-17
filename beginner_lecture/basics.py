from math import *

print("    /|")
print("   / |")
print("  /  |")
print(" /   |")
print("/____|")
print()
name = "Veronica"
age = 25
print("There was a woman named " + name)
print("She was " + str(age) + " years old")

name = "Lucy"
print("She really like the name " + name)
print("But she didnt like not being a Data Analyst")
print()
phrase = "Cat Academy"

# string methods
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.islower())
print()

# nested/stacked string methods
print(phrase.lower().isupper())
print(phrase.upper().isupper())
print()

# string function
print(len(phrase))
print()

# string indexing
print(phrase[0])

# Example of passing a parameter
print(phrase.index("Ca"))
print(phrase.replace("Cat", "Giraffe"))
print()

# Working with numbers
print(2 + 3.0)
print(6 * (7 + 5))
print(pow(2, 2))
print(abs(-5))
print(max([1, 2, 3, 4]))
print(min([5, 6, 7, 8]))
print(round(4.6))
print(floor(3.7))
print(ceil(3.7))
print(sqrt(5))

# Getting input from users
selection = input("Enter name: ")
print("Hello, " + str(selection))

# Basic calculator
value1 = input("Enter number: ")
value2 = input("Enter another number: ")
result = float(value1) + float(value2)
print(result)

