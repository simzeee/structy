def is_prime(n):
  if n < 2:
    return False
  
  prime = 0
  
  for i in range(1, n + 1):
    print(i, n)
    if n % i == 0:      
      prime += 1
  
  print(prime)
  return prime == 2