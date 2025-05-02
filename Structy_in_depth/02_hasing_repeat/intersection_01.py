# TC O(n+m)
# SC O(n+m)
def intersection(a, b):
    result = []
    set_a = set(a)
    for num in b:
        if num in set_a:
            result.append(num)
    return result
