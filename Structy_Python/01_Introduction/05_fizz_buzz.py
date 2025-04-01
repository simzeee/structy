def fizz_buzz(n):
    result = []
    for num in range(1, n + 1):
        if num % 3 == 0 and num % 5 == 0:
            result.append("fizzbuzz")
        elif num % 3 == 0:
            result.append("fizz")
        elif num % 5 == 0:
            result.append("buzz")
        else:
            result.append(num)
    return result
