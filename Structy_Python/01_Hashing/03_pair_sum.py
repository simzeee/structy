# My Solution
def pair_sum(numbers, target_sum):
    result = ()

    i = 0
    j = 1

    while i < len(numbers):
        while j < len(numbers):
            if numbers[i] + numbers[j] == target_sum:
                new_touple = (i, j)
                return result + new_touple
            else:
                j += 1
        i += 1
        j = i + 1


def pair_sum_brute_force_Alvin(numbers, target_sum):
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target_sum:
                return (i, j)


# Improved Solution


def improved_pair_sum(numbers, target_sum):
    #   keys are numbers of the array, value is the indices
    previous = {}

    for index, num in enumerate(numbers):
        complement = target_sum - num
        if complement in previous:
            return (previous[complement], index)
        if num not in previous:
            previous[num] = index
