# Ask user for string
word = input("Enter a word: ")

# Print if string is a palendrome 
def check_palendrome(string):
    check = -1
    for letter in string:
        if letter != string[check]:
            return False
        else:
            check -= 1
    return True

print(word[::-1])