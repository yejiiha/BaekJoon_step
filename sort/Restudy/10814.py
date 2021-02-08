## 나이순 정렬

import sys
input = sys.stdin.readline

n = int(input())
li = []

for _ in range(n):
    age, name = map(str, input().split())
    age = int(age)
    li.append((age, name))

li.sort(key = lambda x: x[0])

for i in li:
    print(i[0], i[1])