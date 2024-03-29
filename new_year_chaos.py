
def minimumBribes(q):
    # Write your code here
    n = len(q)
    count = 0
    for i, person in enumerate(q):
        if person - i + 1 > 3:
            print("Too chaotic")
            return None
        for j in range(max(0, person - 2), i):
            if q[j] > person:
                count += 1
    print(count)


# def minimumBribes(q):
#     count = 0
#     for i, person in enumerate(q):
#         bribes = person - (i + 1)
#         if bribes > 0:
#             count += bribes
#             if bribes > 2:
#                 print("Too chaotic")
#                 return None
#     print(count)
q = [2,1,5,3,4]
minimumBribes(q)