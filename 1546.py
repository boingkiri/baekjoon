def new_score(max_score):
    return (lambda prior_score : prior_score / max_score * 100)

N = int(input())
score_list =[]
max_score = 0
raw_score_list = input().split()
# for i in range(N):
for tmp_score in map(int, raw_score_list):
    # tmp_score = int(input())
    if tmp_score > max_score:
        max_score = tmp_score
    score_list.append(tmp_score)

new_score_list = map(new_score(max_score), score_list)
new_average = sum(new_score_list) / N
print(new_average)

