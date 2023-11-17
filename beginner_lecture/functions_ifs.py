# Functions - a collection of codes/commands that perform a specific task
# Any details within parentheses are called "parameters"
"""
def say_hello(name, age):
    print("Hello, " + str(name) + "!")
    print("You are " + str(age) + "!")

name = input("Enter a name: ")
age = input("Enter an age: ")
# This is an example of passing an argument to a parameter
say_hello(name, age)
"""

"""
# Return statements
def cube(num):
    # it's better to return values from a function than it is to use the value within the function
    # return statements break out of the function and jumps back to function call
    return num**2

print(cube(2))
"""

"""
# If statements
print("You just woke up!")
hungry = False
tired = False
if not hungry and tired:
    print("You went back to sleep")
elif hungry and not tired:
    print("You ate breakfast!")
elif hungry and tired:
    print("You will take a nap, then eat breakfast after!")
else:
    print("You decided to disappear!")
"""

# If statements with comparisons
hungry = input("Are you feeling hungry?: ")
tired = input("Are you feeling tired?: ")
if hungry.lower() == "yes" and tired.lower() == "yes":
    print("You will take a nap, then eat breakfast after!") 
elif hungry.lower() == "no" and tired.lower() == "no":
    print("You decided to disappear!") 
elif hungry.lower() == "yes" and tired.lower() == "no":
    print("You ate breakfast!") 
elif hungry.lower() == "no" and tired.lower() == "yes":
    print("You went back to sleep")
else:
    print("Huh?")