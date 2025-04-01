def compress(s):
  num = 0
  i = 0
  j = 0
  
  result = ""
  
  while j < len(s):
    print('top of loop')
    char = s[i]
    print(char,"j", j)
    print(s[j])
    if s[j] == char:
      j += 1
      num += 1
    else:
      if num == 1:
        result += char
      else:
        result += str(num)
        result += char
      i = j
      num = 0      
      print(result)
      print(i, j, len(s))
  
  print("OUT OF LOOP")
  print(i, j, num, result)
  if num == 1:
    result += char
  else:
    result += str(num)
    result += char
  return result
compress('ccaaatsss')