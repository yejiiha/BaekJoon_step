## 랜선 자르기

import sys

input = sys.stdin.readline

k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]

start, end = 1, max(lan)

while start <= end:
    mid = (start + end) // 2
    lines = 0

    for i in lan:
        lines += i // mid
    
    if lines >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)