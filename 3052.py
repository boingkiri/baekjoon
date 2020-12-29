ans_list = []
for i in range(10):
    tmp_input = int(input())
    remain = tmp_input % 42
    if remain not in ans_list:
        ans_list.append(remain)
    
print(len(ans_list))