def pair_sum(numbers, target_sum):
    # iterate through elements using a single loop
    # hashmap where the keys are numbers of the array
    # values are the indices
    previous = {}
    for i in range(0, len(numbers)):
        complement = target_sum - numbers[i]
        if complement in previous:
            return (previous[complement], i)
        previous[numbers[i]] = i


# pair_sum([4, 7, 9, 2, 5, 1], 5) # -> (0, 5)
