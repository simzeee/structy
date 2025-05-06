from math import sqrt, floor


def is_prime(n):
    # edge case where number is 1 or 0
    if n < 2:
        return False

    for i in range(2, floor(sqrt(n)) + 1):
        print(i)
        if n % i == 0:
            return False

    return True
