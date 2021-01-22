## 동전 0

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

cnt = 0

for i in coins[::-1]:
    if i > k:
        continue
    else:
        if (k % i) < k:
            cnt += k // i
            k %= i

print(cnt)