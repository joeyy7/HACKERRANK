def superDigit(n, k): # n = 4 k =
    # Write your code here
    n = n*k
    sums = 0
    for i in n:
        sums+=int(i)
    if len(str(sums)) == 1:
        print(sums)
        return sums
    else:
        superDigit(str(sums),1)

superDigit("9875", 4)