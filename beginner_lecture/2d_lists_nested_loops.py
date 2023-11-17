# 2D list
"""
number_grid = [
    [324, 67, 123],
    [76, 978, 12],
    [5, 67, 986]
]

for element in number_grid:
    for number in element:
        print(number, end = " ")
    print("\n")
"""

# Translator
vowels = "aeiou"
def translate(phrase):
    result = ""
    for letter in phrase:
        if letter.lower() in vowels:
            result += "v"
        else:
            result += letter
    return result

print(translate("determination"))
