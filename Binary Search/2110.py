## 공유기 설치

import sys

input = sys.stdin.readline

n, c = map(int, input().split())
x = [int(input()) for _ in range(n)]

x.sort()

start = x[1] - x[0]
end = x[-1] - x[0]

result = 0

while start <= end:
    mid = (start + end) // 2

    cnt = 1
    house = x[0]

    for i in range(1, n):
        if x[i] >= mid + house:
            cnt += 1
            house = x[i]
    
    if cnt >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)