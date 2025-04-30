# Time: O(n + m)
# Space: O(n + m)
def anagrams(s1, s2):
    if len(s1) != len(s2):
        return False

    hash1 = {}
    hash2 = {}
    for char in s1:
        if char not in hash1:
            hash1[char] = 1
        else:
            hash1[char] = hash1[char] + 1

    for char in s2:
        if char not in hash2:
            hash2[char] = 1
        else:
            hash2[char] = hash2[char] + 1

    for key in hash1:
        if not (key in hash1 and key in hash2):
            return False
        if hash1[key] != hash2[key]:
            return False
    return True
