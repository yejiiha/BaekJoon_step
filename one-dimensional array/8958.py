# O, X Quiz
n = int(input())

for i in range(n):
    t = input()
    sum = 0
    sum_total = 0
    for j in t:
        if j == "O":
            sum += 1
        else:
            sum = 0
        sum_total += sum

    print(sum_total)
