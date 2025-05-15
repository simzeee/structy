def palindrome(s):
    if s == "":
        return True

    if s[0] != s[-1]:
        return False

    return palindrome(s[1:-1])
