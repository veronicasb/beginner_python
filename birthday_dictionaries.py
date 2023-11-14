BIRTHDAYS = {
    "bob": "3/12/5483", 
    "sally": "23/89/6789"
    }

while True:
    print("\nWelcome to the birthday dictionary. We know the birthdays of: \n")
    for key in BIRTHDAYS:
        print("-", key)

    selection = input("\nWho's birthday do you want to look up? ")
    if selection in BIRTHDAYS:
        message = selection + "'s birthday is on " + BIRTHDAYS[selection]
        print("\n" + "=" * len(message))
        print(message)
        print("=" * len(message))
    else:
        message = "We don't have a birthday for that person in our database!"
        print("\n" + "=" * len(message))
        print(message)
        print("=" * len(message))
