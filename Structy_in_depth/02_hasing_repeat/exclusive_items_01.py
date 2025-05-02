# O(n + m)
# O(n + m)
def exclusive_items(a, b):
    result = []
    set_a = set(a)
    set_b = set(b)

    for item in set_a:
        if item not in set_b:
            result.append(item)

    for item in set_b:
        if item not in set_a:
            result.append(item)

    return result
