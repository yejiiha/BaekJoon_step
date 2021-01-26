## 카드2

import sys
from collections import deque

input = sys.stdin.readline
deq = deque()

n = int(input())

for i in range(1, n + 1):
    deq.append(i)

for _ in range(n-1):
    deq.popleft()
    deq.append(deq.popleft())

print(deq[0])

