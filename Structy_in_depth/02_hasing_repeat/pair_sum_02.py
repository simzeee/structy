def pair_sum(numbers, target_sum):
    # create previous hash map
    previous = {}
    for index, num in enumerate(numbers):
        complement = target_sum - num
        if complement in previous:
            return (index, previous[complement])
        previous[num] = index
