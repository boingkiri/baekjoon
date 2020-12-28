n = int(input())

def is_exist(memoize_list, target):
    if target not in memoize_list:
        return False
    else:
        return True

for i in range(n):
    raw_input = input().split(" ")
    a = int(raw_input[0]) % 10
    b = int(raw_input[1])
    tmp = 1
    memoize = []
    flag = False
    for i in range(b):
        tmp = tmp * a
        tmp = tmp % 10
        if not is_exist(memoize, tmp):
            memoize.append(tmp)
        else:
            flag = True
            break
    
    if flag:
        remained_number_of_cycle = b - i - 1
        match_to_memoize = remained_number_of_cycle % len(memoize)
        tmp = memoize[match_to_memoize]
    if tmp == 0:
        print(10)
    else:
        print(tmp)
