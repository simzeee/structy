def pair_product(numbers, target_product):
  previous = {}
  for index, num in enumerate(numbers):
    complement = target_product / num
    if complement in previous:
      return (index, previous[complement])
    previous[num] = index
