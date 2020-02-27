A,B,V = input().split()

num_A = int(A)
num_B = int(B)
num_V = int(V)

diff = num_A - num_B

day = (num_V - num_A) // diff
if (num_V - num_A) % diff != 0:
    day += 1
print(day + 1)