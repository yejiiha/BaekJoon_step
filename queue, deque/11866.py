## 요세푸스 문제 0

import sys
from collections import deque

input = sys.stdin.readline
deq = deque()

n, k = map(int, input().split())

for i in range(1, n + 1):
    deq.append(i)

print("<", end = "")

while deq:
    for i in range(k - 1):
        deq.append(deq[0])
        deq.popleft()
    print(deq.popleft(), end='')
    if deq:
        print(', ', end='')

print(">")