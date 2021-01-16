## 계단 오르기

import sys

input = sys.stdin.readline

n = int(input())
dp = [0] * 300
li = [int(input()) for _ in range(n)]

if n >= 3:
    dp[0] = li[0]
    dp[1] = max(li[0] + li[1], li[1])
    dp[2] = max(li[0] + li[2], li[1] + li[2])

    for i in range(n):
        dp[i] = max(dp[i-3] + li[i-1] + li[i], dp[i-2] + li[i])
    
    print(dp[n-1])
    
elif n == 2:
    print(max(li[0] + li[1], li[1]))

elif n == 1:
    print(li[0])
