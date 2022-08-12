# My Solution
def uncompress(s):
  nums = '0123456789'
  i = 0
  j = 0
  result = []
  
  while j< len(s):
    if s[j] in nums:
      j += 1
    else:
      num = int(s[i:j])
      result.append(num * s[j])
      j += 1
      i = j
  return "".join(result)

print(uncompress("2c3a1t")) # -> 'ccaaat'

# Alvin's Solution
def uncompress(s):
  numbers = '0123456789'
  result = []
  i = 0
  j = 0
  while j < len(s):
    if s[j] in numbers:
      j += 1
    else:      
      num = int(s[i:j])
      result.append(s[j] * num)
      j += 1
      i = j
      
  return ''.join(result)