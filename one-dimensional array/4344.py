# Print to three decimal places by rounding up the proportion of students above average for each case
c = int(input())  # number of test cases
avg_list = []

for i in range(c):
    scores = list(map(int, input().split()))  # scores list
    n = scores[0]  # number of students

    del scores[0]

    sum = 0
    count = 0

    for j in scores:
        sum += j
    avg_list.append(sum / n)  # avg = sum / n

    for j in scores:
        if j > avg_list[i]:
            count += 1

    avg_list[i] = count / n * 100


for i in range(len(avg_list)):
    print("%.3f%%" % round(avg_list[i], 3))
