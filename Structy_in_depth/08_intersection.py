# TC O(n+m)
# SC O(n+m)
def intersection(a, b):
    union = set(a).intersection(set(b))
    return list(union)


# intersection([4,2,1,6], [3,6,9,2,10]) # -> [2,6]
