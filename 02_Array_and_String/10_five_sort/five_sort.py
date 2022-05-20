# This doesn't work because it removes the wrong things
def five_sort(nums):
  for i, n in enumerate(nums):
    if n == 5:
      five = nums.pop(i)
      nums[-1] = five 
  return nums
  
  
print(five_sort([12, 5, 1, 5, 12, 7]))
# -> [12, 7, 1, 12, 5, 5] 


def five_sort(nums):
  i = 0
  while i < len(nums):
    print(nums)
    print(nums[i])
    if nums[i] == 5:
      print(nums[i])
      five = nums.pop(i)
      nums.append(five)
    i += 1
  return nums


# Alvin's situation with linear runtime

def five_sort(nums):
  i = 0
  j = len(nums) -1
  
  while i < j:
    if nums[j] == 5:
      j -= 1
    elif nums[i] == 5:
      nums[i], nums[j] = nums[j], nums[i]
      i += 1
    else:
      i += 1
  return nums

print(five_sort([5, 5, 5, 1, 1, 1, 4]))
