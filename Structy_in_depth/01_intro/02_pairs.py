def pairs(elements):
    result = []

    for i in range(0, len(elements)):
        for j in range(i + 1, len(elements)):
            result.append([elements[i], elements[j]])

    return result
