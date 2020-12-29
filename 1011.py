def dist_to_trinum(distance):
    half_distance = distance // 2
    tmp = 0
    count = 1
    remainder = 0

    # print("half distnace : "+str(half_distance))
    while tmp + count <= half_distance:
        tmp += count
        count += 1

    count -= 1

    return count, tmp

T = int(input())

for i in range(0,T):
    raw_x, raw_y = input().split()
    x = int(raw_x)
    y = int(raw_y)
    ans = 0

    distance = y - x

    trinum, trinum_sum = dist_to_trinum(distance)
    remained_distance = distance - (2 * trinum_sum)
    max_range = trinum + 1
    max_range_count = remained_distance // max_range

    if remained_distance == 0:
        ans = trinum * 2
        # if remained_distance // max_range == 0:
        #     ans = trinum * 2
        # elif remained_distance // max_range == 1:
        #     ans = trinum * 2 + 1
    elif remained_distance // max_range == 0:
        ans = trinum * 2 + 1
    elif remained_distance // max_range == 1 and remained_distance % max_range == 0:
        ans = trinum * 2 + 1
    else : 
        ans = trinum * 2 + 2
    
    print(ans)
    