## 주유소

import sys

input = sys.stdin.readline

n = int(input())
km = list(map(int, input().split()))
l = list(map(int, input().split()))

res = 0
m = l[0]

for i in range(n-1):
    if l[i] < m:
        m = l[i]
    
    res += m * km[i]

print(res)