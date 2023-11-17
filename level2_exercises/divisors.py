# Ask user for input
num = ""
while not num:
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Please enter a number...\n")

# Print out list of divisors of that number
possible_divisors = range(2, 11)
results = filter(lambda x: num % x == 0, possible_divisors)
print(list(results))
# or
results = [x for x in possible_divisors if num % x == 0]
print(results)