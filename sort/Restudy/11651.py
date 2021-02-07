## 좌표 정렬하기 2

import sys
input = sys.stdin.readline

n = int(input())

li = []

for _ in range(n):
    x, y = map(int, input().split())
    li.append((x, y))

li.sort(key = lambda x: (x[1], x[0]))

for i in li:
    print(i[0], i[1])