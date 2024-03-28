def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    apples = [i+a for i in apples]
    oranges = [j+b for j in oranges]
    count_ap, count_or = 0, 0 
    for i in apples:
        if s<=i<=t:
            count_ap+=1
    for j in oranges:
        if s<=j<=t:
            count_or+=1        
    print(count_ap)
    print(count_or)
            

s = 7
t = 11

a = 5
b = 15


m = 3
n = 2

apples = [-2,2,1]
oranges = [5,-6]

countApplesAndOranges(s, t, a, b, apples, oranges)
