# dictionaries = data structure that allows us to store information in key-value pairs
"""
month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April"
}

print(month_conversions.get("Who", "Not valid"))
"""

# While loops - structure that loops through a block of code until specified to stop
"""
i = 0
while i <= 10:
    print(str(i), end = " ")
    i += 1
"""

secret_word = "discipline"
guess = ""
tries = 0
while tries <= 3:
    guess = input("Enter your guess: ")
    tries += 1
    if guess == secret_word:
        print("You win!")
        break
    elif guess != secret_word:
        if tries == 3:
            print("Try again!")
        else:
            print("You lost!")
    

    