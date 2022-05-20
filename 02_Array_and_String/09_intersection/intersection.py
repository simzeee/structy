# brute force
def intersection(a,b):
  result = []

  for el in a:
    if el in b:
      result.append(el)

  return result

"""
O(n*m) runtime because "in" is linear
"""

def intersection_set(a,b):

  result = []
  items = set()

  for el in a:
    items.add(el)
  
  if b in items: # in works for all collection types (lists, tuples, strings, dicts, sets), but because set it is constant
    result.append(b)
  
  return result

def intersection_set_two(a,b):

  items = set(a)
  
  return [ ele for ele in b if ele in items]