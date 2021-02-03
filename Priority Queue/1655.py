## 가운데를 말해요

import sys
import heapq 
 
input = sys.stdin.readline

# 넣기만함
def middleheap(minheap, maxheap, x):
    # 같다면 max힙에 넣어준다
    if len(maxheap) == len(minheap):
        heapq.heappush(maxheap, -x)
    # max힙이 크다면 minheap넣어 균형을 맞춰준다.
    else:
        heapq.heappush(minheap, x)
    # minheap이 비어잇지않고 최대 힙의 루트는 항상 최소 힙의 루트보다 작게 유지해준다.
    if minheap and -maxheap[0] > minheap[0]:
        # 최대힙의 루트노드가 더크다면 스왑해주고 다시 힙구조로 만들어주어야한다.
        a = heapq.heappop(minheap)
        b =- heapq.heappop(maxheap)
        heapq.heappush(maxheap, -a)
        heapq.heappush(minheap, b)
 
 
n = int(input())
minheap,maxheap = [],[]
while n > 0:
    n -= 1
    middleheap(minheap, maxheap, int(input()))
    print(-1 * maxheap[0])
