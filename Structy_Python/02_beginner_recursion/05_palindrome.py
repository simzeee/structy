def palindrome(s):
    if s == "":
        return True
    if s[0] == s[-1]:
        return palindrome(s[1:-1])
    else:
        return False
