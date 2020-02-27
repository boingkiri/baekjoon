T = int(input())

for i in range(0,T):
    H,W,N = input().split()
    num_H = int(H)
    num_W = int(W)
    num_N = int(N) - 1

    order = (num_N // num_H) + 1
    floor = num_N % num_H + 1

    if (order // 10 != 0) :
        print(str(floor) + str(order))
    else:
        print(str(floor) + '0' + str(order))
