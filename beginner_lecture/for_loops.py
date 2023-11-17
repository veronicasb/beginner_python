"""
phrase = "hello world"
for letter in phrase:
    print(letter, end = "")

print("\n")
stressors = ["money", "fitness", "career"]
for element in stressors:
    print(element)

print()
for i in range((len(stressors))):
    print(stressors[i])
"""

def raise_to_power(base, power):
    result = 1
    for i in range(power):
        result = result * base
    return result

print(raise_to_power(3, 0))
print(3**0)