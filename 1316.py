
N = int(input())
count = 0

for i in range(0,N):
    word = input()
    prev = ''
    flag = True
    inspector = [False] * 26
    for j in word:
        if (prev == j):
            continue
        else:
            correspondIndex = ord(j) - 97
            if (inspector[correspondIndex]):
                flag = False
                break
            else:
                inspector[correspondIndex] = True
            prev = j
    if flag:
        count += 1
    inspector = [False] * 26
    flag = False
print(count)