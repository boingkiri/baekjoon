N = int(input())

for i in range(N):
    tmp_input = input()
    score_sum = 0
    continuous = 1
    for element in tmp_input:
        if element == 'X':
            continuous = 1
        elif element == 'O':
            score_sum += continuous
            continuous += 1
    print(score_sum)