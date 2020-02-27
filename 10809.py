seq = [-1] * 26

S = input()

for i in range(0,len(S)):
    tmp = ord(S[i]) - 97
    if (seq[tmp] == -1):
        seq[tmp] = i

for i in seq:
    print(i, end=' ')