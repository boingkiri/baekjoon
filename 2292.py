count = 0
total = 0

N = int(input())

while total < N:
    if (total == 0):
        total += 1
    else:
        total += 6 * count
    count += 1
print(count)