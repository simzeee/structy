def max_value(nums):
  max = float('-inf')
  
  for num in nums:    
    if num > max:      
      max = num
  
  return max