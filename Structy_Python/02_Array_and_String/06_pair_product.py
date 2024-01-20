def pair_product(numbers, target_product):
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] * numbers[j] == target_product:
                return (i, j)


def pair_product_linear(numbers, target_product):
    previous = {}

    for index, num in enumerate(numbers):
        complement = target_product / num
        if complement in previous:
            return (index, previous[complement])
        if num not in previous:
            previous[num] = index
