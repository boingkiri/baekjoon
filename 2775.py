T = int(input())

for i in range(0, T):
    k = int(input())
    n = int(input())
    cur = range(1,n+1)
    for floor in range(0, k):
        sum = 0
        prev = cur
        cur = []
        for order in prev:
            sum += order
            cur.append(sum)
    print(cur[len(cur)-1])