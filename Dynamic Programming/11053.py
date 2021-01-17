## 가장 긴 증가하는 부분 수열

import sys

input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))
cnt = [1] * n

for i in range(1, n):
    for j in range(i):
        if a[j] < a[i]:
            cnt[i] = max(cnt[i], cnt[j] + 1)

print(max(cnt))