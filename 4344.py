C = int(input())

for i in range(C):
    raw_input = input().split()
    average_above = 0
    number_of_students = int(raw_input[0])
    score_list = list(map(int, raw_input[1:]))
    average = sum(score_list) / number_of_students

    for score in score_list:
        if score > average:
            average_above += 1
    ans = "{0:.3f}%".format(average_above/number_of_students*100)
    print(ans)