# def is_prime(n):
#   if n == 1:
#     return False
#   for num in range(2, n):
#     if n % num == 0:
#       return False
#   return True
from math import sqrt, floor

# O(sqrt(n))
# space: 0(1)
def is_prime(n):
  # check up to the sqrt(n)
  # every factor has a corresponding pair n = a * b
  # 8 * 8 = 64 and it's the middle inflection point for factor pairs
  if n < 2:
    return False
  # adding one because range is exclusive you add 1
  # you need to round down because range requires integers
  for num in range(2, floor(sqrt(n)) + 1):
    if n % num ==0:
      return False
      
  return True
  