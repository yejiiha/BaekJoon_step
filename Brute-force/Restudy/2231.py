## 분해합

n = int(input())

for i in range(1, n + 1):
    devided_num = list(map(int, str(i)))
    devided_sum = i + sum(devided_num)

    if devided_sum == n:
        print(i)
        break
    if i == n:
        print(0)