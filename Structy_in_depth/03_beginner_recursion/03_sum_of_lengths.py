# Time O(n**2) recursive call for every element of the array, then copy the new sub-arrays 
# Space O(n**2)j n recursive calls for n sub arrays 
def sum_of_lengths(strings):
    if len(strings) == 0:
        return 0
    return len(strings[0]) + sum_of_lengths(strings[1:])
