# def pairs(elements):
#   result = []
#   for i, ele in enumerate(elements):
#     for ele2 in elements[i + 1:]:
#       result.append([ele, ele2])
#   return result

def pairs(elements):
  return [
    (elements[i], elements[j])
    for i in range(0, len(elements))
    for j in range(i + 1, len(elements))
  ]
