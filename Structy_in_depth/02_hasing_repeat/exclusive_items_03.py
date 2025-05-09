def exclusive_items(a, b):
    difference = []
    set_a = set(a)
    set_b = set(b)

    for item in set_a:
        if item not in set_b:
            difference.append(item)
    for item in set_b:
        if item not in set_a:
            difference.append(item)
    return difference


print(exclusive_items([4, 2, 1, 6], [3, 6, 9, 2, 10]))  # -> [4,1,3,9,10]
