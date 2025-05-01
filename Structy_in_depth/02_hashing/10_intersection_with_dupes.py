from collections import Counter


def intersection_with_dupes(a, b):
    counter_a = Counter(a)
    counter_b = Counter(b)

    result = []
    for key in counter_a:
        for i in range(0, min(counter_a[key], counter_b[key])):
            result.append(key)
    return result
