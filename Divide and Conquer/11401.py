## 이항계수 3

import sys

input = sys.stdin.readline

def mul(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b % 2 > 0:
        return mul(a, b-1) * a
    else:
        d = mul(a, b // 2)
        d %= p
        return d ** 2 % p

n, k = map(int,input().split())
    
A = 1
B = 1
p = 1000000007

for i in range(1, n+1):
    A *= i
    A %= p

for i in range(1, k+1):
    B *= i
    B %= p

for i in range(1, n-k+1):
    B *= i
    B %= p
    
B = mul(B, (p-2) % p)

print((A * B) % p) 