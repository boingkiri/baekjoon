def takeDigit(N : int) -> (int, int, int):
    H = N // 100
    N = N % 100
    T = N // 10
    N = N % 10
    O = N
    return H,T,O


N = int(input())
count = 0

if (N >= 100):
    count = 99
    for i in range(100, N+1):
        a,b,c = takeDigit(i)
        # print(str(a)+str(b)+str(c))
        CD1 = a-b
        CD2 = b-c
        if (CD1 == CD2):
            count = count + 1
else:
    count = N

print(count)