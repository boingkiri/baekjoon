def rev_num(N : int):
    H = N // 100
    N = N % 100
    T = N // 10
    N = N % 10
    O = N
    new_num = O * 100 + T * 10 + H
    return new_num

A,B = input().split()
rev_A = rev_num(int(A))
rev_B = rev_num(int(B))
if (rev_A >= rev_B) : 
    print(rev_A)
else:
    print(rev_B)
