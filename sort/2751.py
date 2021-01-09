## 수 정렬하기 2

import sys

n = int(input())
li = []

for _ in range(n):
    li.append(int(sys.stdin.readline()))

for i in sorted(li):
    sys.stdout.write(str(i)+'\n')



