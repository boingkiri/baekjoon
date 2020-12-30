import math

raw = input().split()
M = int(raw[0])
N = int(raw[1])
upper_bound = math.ceil(math.sqrt(N))

number_list = [True] * (N+1)
number_list[0] = False
number_list[1] = False

for i in range(2, upper_bound):
    if number_list[i] == True:
        for j in range(2 * i, N+1, i):
            number_list[j] = False

for i in range(M, N+1):
    if number_list[i]:
        print(i)