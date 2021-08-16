from math import sqrt, floor

def is_prime(n):
  if n < 2:
    return False
  
  for i in range(2, floor(sqrt(n)) + 1):
    # in python, the first argument to range is inclusive, 
    # the second is non inclusive
    if n % i == 0:
      return False
    
  return True

# n = input number
# Time: O(square_root(n))
# Space: O(1)