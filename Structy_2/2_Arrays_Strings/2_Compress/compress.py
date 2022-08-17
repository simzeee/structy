def compress(s):
  result = []
  num = 1
  i = 0
  
  while i <= len(s):
    print('here is i', i)
    if(i == len(s)-1):
      print('length = s')
      if num > 1:
        result.append(str(num))
      result.append(s[i])
      break
    print(s[i])
    print(s[i + 1])
    print(num)
    if s[i] == s[i + 1]:
      num += 1
      i += 1
    else:
      print('here')
      if num > 1:
        result.append(str(num))
      result.append(s[i])
      print(result)
      num = 1
      i += 1
  print(result)
  return "".join(result)