## 수 정렬하기 3

import sys

n = int(input())

dic = {}

for _ in range(n):
    a = int(sys.stdin.readline())
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1

for sorted in sorted(dic.items()):
    for _ in range(sorted[1]):
        print(sorted[0])