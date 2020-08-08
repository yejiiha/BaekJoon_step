# Average score
score_list = []
sum = 0

for i in range(0, 5):
    i = int(input())
    if 0 <= i <= 100 and i % 5 == 0:
        score_list.append(i)

for n in range(0, 5):
    if score_list[n] >= 40:
        sum += score_list[n]
    else:
        score_list[n] = 40
        sum += score_list[n]

print(sum//5)
