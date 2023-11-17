from datetime import date

DATE = date.today()

while True:
    text = input("Dear diary: ")

    save_select = ""
    while save_select != "y" or save_select != "n":
        save_select = input("Save? (y/n): ")
        if save_select == "y":
            title = input("Name your file: ")
            with open(title, "w") as open_file:
                open_file.write(str(DATE) + "\n\n" + text)
            break
        elif save_select == "n":
            break
        else:
            print("Invalid selection...")
