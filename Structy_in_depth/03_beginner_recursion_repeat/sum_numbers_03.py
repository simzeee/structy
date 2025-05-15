def sum_numbers_recursive(numbers):
    if numbers == []:
        return 0

    return numbers[0] + sum_numbers_recursive(numbers[1:])
