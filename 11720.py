N = int(input())
A = int(input())

sum = 0
for i in range(0,N):
    sum = sum + int(A % 10)
    A = A // 10
print(sum)