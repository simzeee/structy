# n**2 T and S
# O(n) for each recursive call times O(n) for each slice
# each frame on the callstack n times each sub array which would be O(n/2) => O(n)

def sum_numbers_recursive(numbers):
    if len(numbers) == 0:
        return 0
    return numbers[0] + sum_numbers_recursive(numbers[1:])
