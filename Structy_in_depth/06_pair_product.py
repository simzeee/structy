# O(n**2)
# O(1)
# def pair_product(numbers, target_product):
#     for idx, num in enumerate(numbers):
#         check = target_product / num
#         if check in numbers and check != num:
#             return (idx, numbers.index(check))


# print(pair_product([4, 6, 8, 2], 16))  # -> (2, 3)


# O(n)
# O(1)
def pair_product(numbers, target_product):
    previous = {}
    for idx, num in enumerate(numbers):
        complement = target_product / num
        if complement in previous:
            return (idx, previous[complement])
        previous[num] = idx
