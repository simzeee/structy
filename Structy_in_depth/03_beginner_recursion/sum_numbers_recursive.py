# Time:
# O(n + 1) => O(n) for each function call
# O(n) for slicing each array
# Total Time Complexity: O(n**2)

# Space:
# O(n) for each function call
# O(n) for each subarray
# Total Space Complexity: O(n**2)


def sum_numbers_recursive(numbers):

    if len(numbers) == 0:
        return 0

    return numbers[0] + sum_numbers_recursive(numbers[1:])
