import math

a,b,c = input().split()

num_a = int(a)
num_b = int(b)
num_c = int(c)

if (num_c <= num_b) :
    print("-1")
else:
    print(int(num_a / (num_c - num_b)) + 1)
    

