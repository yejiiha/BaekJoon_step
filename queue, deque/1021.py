## 회전하는 큐

import sys
from collections import deque

input = sys.stdin.readline
deq = deque()

n, m = map(int, input().split())
position = list(map(int, input().split()))
cnt = 0

for i in range(n):
    deq.append(i + 1)

for p in position:
    i = 0
    while p != deq[i]:
        i += 1
    i = len(deq) - i if len(deq) - i < i else -i
    deq.rotate(i)
    cnt += abs(i)
    deq.popleft()

print(cnt)