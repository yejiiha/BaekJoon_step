## 최대 힙

import sys
import heapq

input = sys.stdin.readline
heap = []

n = int(input())

for _ in range(n):
    x = int(input())

    if x != 0:
        heapq.heappush(heap, (-x))
    else:
        try:
            print(-1 * heapq.heappop(heap))
        except:
            print(0)

# heapq.heappush(heap, 50)
# heapq.heappush(heap, 10)
# heapq.heappush(heap, 20)

# print(heap)