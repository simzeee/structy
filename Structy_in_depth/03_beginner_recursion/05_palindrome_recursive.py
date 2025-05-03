# Time: O(n*2) recursive call and string operation
# Space: O(n*2) same
def palindrome(s):
    print(s)
    if s == "":
        return True

    if s[0] != s[-1]:
        return False

    if len(s) == 1:
        return True

    return palindrome(s[1 : len(s) - 1])


print(palindrome("kayak"))
