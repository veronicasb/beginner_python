from datetime import date

# Ask user to enter name and age
name = str(input("\nWhat's your name?: "))
age = ""
while age == "":
    try:
        age = int(input("\nHow old are you?: "))
    except ValueError:
        print("\nPlease enter a number...")

# Print out a message that tells them the year they will turn 100
year = int(str(date.today())[0:4])
year_turning_100 = (100 - age) + year
message = "\n{0}, you will turn 100 years old in {1}!\n"
print("\n" + "+" * len(message))
print(message.format(name, year_turning_100))
print("+" * len(message))

# Ask the user for a number
number = ""
while number == "":
    try:
        number = int(input("\nEnter a number: "))
    except ValueError:
        print("\nPlease enter a number...")

# Repeat the previous message as many times as the number they entered
print("\n" + "+" * len(message))
print(message.format(name, year_turning_100) * number)
print("+" * len(message))