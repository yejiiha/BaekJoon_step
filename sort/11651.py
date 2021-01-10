## 좌표 정렬하기2

import sys

n = int(sys.stdin.readline())
li = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    li.append((x, y))

li.sort(key=lambda x:(x[1],x[0]))

for i in li:
    print(i[0], i[1])