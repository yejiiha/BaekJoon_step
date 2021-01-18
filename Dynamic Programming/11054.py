## 가장 긴 바이토닉 부분 수열

import sys
import operator

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

inc = [1] * n
dec = [1] * n

for i in range(n):
    for j in range(i):
        if a[i] > a[j] and inc[i] < inc[j] + 1:
            inc[i] = inc[j] + 1

for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        if a[i] > a[j] and dec[i] < dec[j] + 1:
            dec[i] = dec[j] + 1
    
sys.stdout.write(str(max(map(operator.add, inc, dec)) - 1))