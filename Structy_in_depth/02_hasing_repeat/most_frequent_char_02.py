from collections import Counter


def most_frequent_char(s):
    return Counter(s).most_common()[0][0]


# print(most_frequent_char('bookeeper')) # -> 'e'
