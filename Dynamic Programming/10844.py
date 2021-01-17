## 쉬운 계단 수

import sys

input = sys.stdin.readline

n = int(input())

stair_num = [([0] * 10) for __ in range(101)]

for i in range(1, 10):
    stair_num[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            stair_num[i][j] = stair_num[i - 1][1]
        elif j == 9:
            stair_num[i][j] = stair_num[i - 1][8]
        else:
            stair_num[i][j] = stair_num[i - 1][j - 1] + stair_num[i - 1][j + 1]

print(sum(stair_num[n]) % 1000000000)


