def intersection_with_dupes(a, b):
    count_a = {}
    count_b = {}
    for ele in a:
        if ele not in count_a:
            count_a[ele] = 0
        count_a[ele] += 1

    for ele in b:
        if ele not in count_b:
            count_b[ele] = 0
        count_b[ele] += 1

    result = []

    for ele in count_a:
        if ele in count_b:
            for i in range(0, min(count_a[ele], count_b[ele])):
                result.append(ele)
    return result
