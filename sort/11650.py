## 좌표 정렬하기

import sys

n = int(input())
li = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    li.append((x, y))

for i in sorted(li):
    print(i[0], i[1])