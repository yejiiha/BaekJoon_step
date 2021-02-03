## 절댓값 힙

import sys
import heapq

input = sys.stdin.readline
heap = []

n = int(input())

for _ in range(n):
    x = int(input())

    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)