def pair_sum(numbers, target_sum):
    # create previous hash map
    previous = {}
    for idx, num in enumerate(numbers):
        complement = target_sum - num
        if complement in previous:
            return (idx, previous[complement])
        previous[num] = idx
