def intersection(a, b):
    set_a = set(a)
    # set_b = set(b)
    return [num for num in b if num in set_a]


# a = [ i for i in range(0, 50000) ]
# b = [ i for i in range(0, 50000) ]
# intersection(a, b)) # -> [0,1,2,3,..., 49999]
