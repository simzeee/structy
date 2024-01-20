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
