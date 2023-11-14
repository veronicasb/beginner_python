# Create a function that 3 variables as input

def quick_sort(ls):
    if len(ls) <= 1:
        return ls
    else:
        return quick_sort([e for e in ls[1:] if e <= ls[0]]) + [ls[0]] +\
            quick_sort([e for e in ls[1:] if e > ls[0]])

def max_of_three():
    var1 = int(input("Enter a number: "))
    var2 = int(input("Enter a second number: "))
    var3 = int(input("Enter a third number: "))

    values = [var1, var2, var3]

    # Sort values
    sorted_ls = quick_sort(values)
    print(sorted_ls)

    # Return the largest of the
    return sorted_ls[-1]

print(max_of_three())