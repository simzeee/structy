def reverse_string(s):
    if s == "":
        return ""
    return s[-1] + reverse_string(s[: len(s) - 1])
