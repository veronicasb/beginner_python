# Ask user for a string
user_string = ""
while not user_string:
    user_string = str(input("Enter a string: "))


# Print out whether string is a palindrome or not
if user_string == user_string[::-1]:
    print(True)
else:
    print(False)