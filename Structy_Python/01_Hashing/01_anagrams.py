def anagrams(s1, s2):
  return char_count(s1) == char_count(s2)


def char_count(s):
  
  chars = {}
  
  for letter in s:
    if letter not in chars:
      chars[letter] = 0
    else:
      chars[letter] = chars[letter] + 1
  
  return chars
