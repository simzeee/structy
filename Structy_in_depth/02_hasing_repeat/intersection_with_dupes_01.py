def intersection_with_dupes(a, b):
    result = []
    dict_a = {}
    dict_b = {}
    for el in a:
        if el not in dict_a:
            dict_a[el] = 1
        else:
            dict_a[el] = dict_a[el] + 1

    for el in b:
        if el not in dict_b:
            dict_b[el] = 1
        else:
            dict_b[el] = dict_b[el] + 1

    for key in dict_a:
        if key in dict_b:
            count = min(dict_a[key], dict_b[key])
            for i in range(0, count):
                result.append(key)
    return result
