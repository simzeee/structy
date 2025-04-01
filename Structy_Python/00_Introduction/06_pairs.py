# def pairs(elements):
#   result = []
#   for ele in elements:
#     for ele2 in elements[1:]:
#       if [ele, ele2] not in result:
#         if [ele2, ele] not in result:
#           if ele2 != ele:
#             result.append([ele, ele2])
#   return result


def pairs(elements):
    result = []
    for i in range(0, len(elements)):
        for j in range(i + 1, len(elements)):
            result.append([elements[i], elements[j]])
    return result
