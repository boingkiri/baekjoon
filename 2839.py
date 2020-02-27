fiveCount = 0
N = int(input())
maxCount = -1

while (fiveCount * 5) <= N :
    threeflag = (N - (fiveCount * 5)) % 3
    if (threeflag == 0):
        threeCount = (N - (fiveCount * 5)) // 3
        maxCount = fiveCount + threeCount
    fiveCount += 1
print(maxCount)

