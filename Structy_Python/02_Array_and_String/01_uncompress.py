# my solution
def uncompress(s):
  num = ""
  letter = ""  
  result = ""
  
  j = 0
  
  while j < len(s):
    if s[j].isdigit():
      print(num)
      num += s[j]
      j += 1
    else:
      letter = s[j]
      result += int(num) * letter
      print(result)
      num = ""
      letter = ""
      j += 1

  return result

uncompress("2c3a1t")

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