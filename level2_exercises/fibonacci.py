# generators

def fibonacci(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, b + a

try:
    user_limit = int(input("Enter a number: "))
except ValueError as e:
    print(e, "Value submitted must be a number.")

result = list(fibonacci(user_limit))

for element in result:
    print(element, end=" ")