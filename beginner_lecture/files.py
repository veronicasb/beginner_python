# r = read, w = write, a = append, r+ = read and write
example = open("test.txt", "r+")

# Make sure file is readable first
try:
    print(example.readable())
    file_lines = example.read().split("\n")
    for line in file_lines:
        print(line)

    # Adding new lines should always start with newline character (if applicable)
    example.write("\nawerghewrg")    

    file_lines = example.read().split("\n")
    for line in file_lines:
        print(line)

except:
    print("ok")

# Always close a file after opening
example.close()

# Create new file by "opening" filename that you want to create
example2 = open("test2.txt", "w")
example2.write("Creating a new page")
example2.write("\nAnother line")
example2.close()