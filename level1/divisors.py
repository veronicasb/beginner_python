# Ask user for a number
check = int(input("Enter a number: "))

# Print out list of all divisors
result = []
for i in range(2, (check + 1)):
    if check % i == 0:
        result.append(i)

for element in result:
    print(str(element))
        