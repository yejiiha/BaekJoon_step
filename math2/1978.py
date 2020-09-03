n = int(input())
num_list = list(map(int, input().split()))
res = 0

for i in num_list:
    answer = 0
    for j in range(1, i+1):
        if i % j == 0:
            answer += 1
    if answer == 2:
        res += 1

print(res)
