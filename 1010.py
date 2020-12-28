T = int(input())


def comb_numerator(M, N):
    tmp = 1
    for i in range(M, M-N, -1):
        tmp = tmp * i
    return tmp

def comb_denominator(M, N):
    tmp = 1
    for i in range(N):
        tmp = tmp * (i+1)
    return tmp

for i in range(0,T):
    N, M = input().split()
    num_n = int(N)
    num_m = int(M)
    numerator = comb_numerator(num_m, num_n)
    denominator = comb_denominator(num_m, num_n)
    ans = numerator // denominator
    print(ans)