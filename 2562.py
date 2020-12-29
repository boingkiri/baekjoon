max_value = -1
index = 0
for i in range(9):
    tmp_value = int(input())
    if max_value < tmp_value:
        max_value = tmp_value
        index = i + 1
print(max_value)
print(index)