import math

def is_prime(N):
    sqrt_N = math.sqrt(N)
    round_sqrt_N = math.ceil(sqrt_N)
    flag = True
    upper_bound = 0

    if N == 1:
        return False

    if round_sqrt_N ** 2 == N:
        upper_bound = round_sqrt_N + 1
    else:
        upper_bound = round_sqrt_N
    
    for i in range(2, upper_bound):
        if N % i == 0:
            flag = False
            break
    return flag


M = int(input())
N = int(input())
sum_val = 0
min_prime = 10000

for i in range(M, N+1):
    if is_prime(i):
        if min_prime == 10000:
            min_prime = i
        sum_val += i
if sum_val == 0:
    print(-1)
else:
    print(sum_val)
    print(min_prime)