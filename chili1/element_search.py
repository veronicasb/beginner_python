def element_search(ordered_list, num):
    if num in ordered_list: 
        return True
    else:
        return False

ls = [213, 568, 135, 678, 334]
print(element_search(ls, 4231))