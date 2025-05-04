# n = length of array a, m = length of array b
# Time: O(n+m)
# Space: O(n+m)
def exclusive_items(a, b):
  # make sets from both lists for constant lookup time
  set_a = set(a)
  set_b = set(b)
  result = []

  for item in set_b:
    if item not in set_a:
      result.append(item)
      
  for item in set_a:
    if item not in set_b:
      result.append(item)

  return result