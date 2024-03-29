an = "ananam"

def is_palindrome(s):
    return s == s[::-1]
def palindromeIndex(s):
    # Write your code here
    if is_palindrome(s):
        return -1
    for i in range(len(s)//2):
        if s[i:] != s[len(s) - 1 - i]:
            if is_palindrome(s[i:len(s)-1-i]):
                return (len(s)-1-i)
            elif is_palindrome(s[i+1:len(s)-i]):
                return i
    return -1
print(palindromeIndex(an))