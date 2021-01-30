## 수 찾기

import sys
import time

input = sys.stdin.readline
start_time = time.time()

n = int(input())
N = sorted(map(int, input().split()))
m = int(input())
M = map(int, input().split())

def binary_search(i, N, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2

    if i == N[mid]:
        return 1
    elif i < N[mid]:
        return binary_search(i, N, start, mid - 1)
    else:
        return binary_search(i, N, mid + 1, end)

for i in M:
    start = 0
    end = n - 1
    print(binary_search(i, N, start, end))

print(time.time()-start_time)