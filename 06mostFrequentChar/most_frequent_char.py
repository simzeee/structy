from collections import Counter

def most_frequent_char(s):
#   Make counter object
  obj = Counter(s)
  print(obj)
  #   Make list of all values
  v=list(obj.values())
  print(v)
#   Make list of all keys
  k=list(obj.keys())
  print(k)
# return the first value of the list of keys
# at the index of the highest number
  return k[v.index(max(v))]

  # Alvin's Solution

  def most_frequent_char(s):
    count = {}
  for char in s:
    if char not in count:
      count[char] = 0    
    count[char] += 1
    
  best = None
  for char in s:
    if best is None or count[char] > count[best]:
      best = char
  return best