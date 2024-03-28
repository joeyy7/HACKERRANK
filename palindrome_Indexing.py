an = "ananam"
def palindromeIndex(s):
    # Write your code here
    pal = s[::-1]
    print(f"palindrome: {pal} and string: {s}")
    n = len(s)
    if pal == s:
        print(-1)
    elif pal[1:] == s[1:]:
        print(f"palindrome: {pal[0]} and string: {s[0]}")
        print(n-1)
    elif pal[0:n-1] == s[0:n-1]:
        print(f"palindrome: {pal[n-1]} and string: {s[n-1]}")
        print(0)
palindromeIndex(an)