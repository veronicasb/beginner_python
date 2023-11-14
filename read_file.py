NAMES_COUNT = {}

# Open and read text file, then count how many times each name appears
with open("read_file.txt", "r") as open_file:
    text = open_file.read().split("\n")
    for name in text:
        if name not in NAMES_COUNT:
            NAMES_COUNT[name] = 1
        else:
            NAMES_COUNT[name] += 1

# Print results to screen
for key, value in NAMES_COUNT.items():
    print(key + ": " + str(value))