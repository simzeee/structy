def intersection(a, b):
    return list(set(a).intersection(set(b)))


def intersection_comprehension(a, b):
    items_set = set(a)
    return [item for item in b if item in items_set]
