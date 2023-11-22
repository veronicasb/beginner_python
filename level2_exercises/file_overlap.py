def read_contents(file):
    with open(file, 'r') as open_file:
        return open_file.read().split('\n')
    
def find_overlap(ls1, ls2):
    result = set()
    for element in ls1:
        if element in ls2:
            result.add(element)
    for element in ls2:
        if element in ls1:
            result.add(element)
    return result


contents1 = read_contents("one.txt")
contents2 = read_contents("two.txt")

overlap = find_overlap(contents1, contents2)

for element in overlap:
    print(element, end=" ")

