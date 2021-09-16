# My Solution
def compress(s):
  i = 0
  j = 0
  s += "!"
  result = []
  
  while j < len(s):
    if(s[i] == s[j]):
      j+=1
    else:
      count = j-i
      if count>=2:
        result.append(str(count)+s[i])
        i = j
        j+=1
      else:
        result.append(s[i])
        i = j
        j+=1
  return "".join(result)

print(compress('ccaaatsss'))


# Alvin's solution
def compress(s):
  s += '!'
  result = []
  i = 0
  j = 0
  while j < len(s):
    if s[i] == s[j]:
      j += 1  
    else:
      num = j - i
      if num == 1:
        result.append(s[i])
      else:
        result.append(str(num)) 
        result.append(s[i])
      i = j
    
  return ''.join(result)