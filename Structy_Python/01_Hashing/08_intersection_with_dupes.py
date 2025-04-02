def intersection_with_dupes(a, b):
    result = []
    dict_a = counter_map(a)
    dict_b = counter_map(b)

    for key in dict_a:
        if key in dict_b:
            count = min(dict_a[key], dict_b[key])
            for i in range(0, count):
                result.append(key)
    return result


def counter_map(iter):
    result = {}
    for el in iter:
        if el not in result:
            result[el] = 1
        else:
            result[el] = result[el] + 1
    return result
