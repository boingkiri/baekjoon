N = int(input())
min_value = 1000000
max_value = -1000000

# for i in range(N):

tmp_input = input().split()
for tmp_value in map(int, tmp_input):
    if min_value > tmp_value:
        min_value = tmp_value
    if max_value < tmp_value:
        max_value = tmp_value

print(str(min_value) + ' ' + str(max_value))