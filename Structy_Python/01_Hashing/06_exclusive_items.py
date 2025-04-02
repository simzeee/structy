def exclusive_items(a, b):
    result = []

    a_set = set(a)
    b_set = set(b)

    for el in a:
        if el not in b_set:
            result.append(el)

    for el in b:
        if el not in a_set:
            result.append(el)

    return result
