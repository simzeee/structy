# My Solution
def max_value(nums):
  max = nums[0]
  for n in nums:
    print(n)
    if n > max:
      max = n
  return max

max_value([4, 7, 2, 8, 10, 9])

# Alvin's Solution

def max_value(nums):
  maximum = float('-inf')
  
  for num in nums:
    if num > maximum:
      maximum = num
      
  return maximum

# n = length of list
# Time: O(n)
# Space: O(1)