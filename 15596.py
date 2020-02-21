def solve (a:list) -> int:
    sum = 0
    for i in a:
        sum = sum + i
    return sum

# def sub_solve(a:list, sum:int) -> int:
#     if (len(a) == 0) : 
#         return sum
#     else:
#         return sub_solve(a[1:], sum + a[0])
