def most_frequent_char(s):
    count = char_count(s)
    frequency = 0
    result = None

    for key in count:
        if count[key] > frequency:
            frequency = count[key]
            result = key

    return result


def char_count(s):
    chars = {}

    for letter in s:
        if letter not in chars:
            chars[letter] = 0
        else:
            chars[letter] = chars[letter] + 1

    return chars
