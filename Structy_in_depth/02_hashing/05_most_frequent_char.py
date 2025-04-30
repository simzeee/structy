# Time: O(n)
# Space: O(n)


def most_frequent_char(s):
    count = {}
    for char in s:
        if char not in count:
            count[char] = 0
        count[char] += 1
    max = ""
    char_count = 0
    for key in count:
        if count[key] > char_count:
            char_count = count[key]
            max = key

    return max


# single_pass
def most_frequent_char(s):
    if not s:
        return None

    count = {}
    mfc = None
    max_count = 0

    for char in s:
        # increment
        count[char] = count.get(char, 0) + 1
        # immediately check if it’s now the new max
        if count[char] > max_count:
            max_count = count[char]
            mfc = char

    return mfc


# Time: O(n)
# Space: O(n)
from collections import Counter


def most_frequent_char(s):
    return Counter(s).most_common(1)[0][0]


# def most_frequent_char(s):
#     if not s:
#         return None

#     # e.g. lowercase a–z
#     freq = [0] * 26
#     offset = ord("a")
#     mfc = None
#     max_count = 0

#     for ch in s:
#         idx = ord(ch) - offset
#         freq[idx] += 1
#         if freq[idx] > max_count:
#             max_count = freq[idx]
#             mfc = ch

#     return mfc
