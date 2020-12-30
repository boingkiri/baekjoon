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


N = int(input())
tmp_input = input().split()
prime_count = 0
int_input = list(map(int, tmp_input))

for i in int_input:
    if is_prime(i):
        prime_count += 1
print(prime_count)