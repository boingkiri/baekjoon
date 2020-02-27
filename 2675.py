N = int(input())

for i in range(0,N):
    R, S = input().split()
    R = int(R)
    for i in S:
        print(i * R,end='')
    print()