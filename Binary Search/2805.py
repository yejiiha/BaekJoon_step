## 나무 자르기

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
tree_h = list(map(int, input().split()))

start, end = 1, max(tree_h)

while start <= end:
    mid = (start + end) // 2
    h = 0

    for i in tree_h:
        if i >= mid:
            h += i - mid
    
    if h >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)