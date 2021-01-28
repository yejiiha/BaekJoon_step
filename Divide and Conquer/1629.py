## 곱셈

import sys

input = sys.stdin.readline

def Recursive_Power(a,b):
    if b == 1:
        return a % c
    if b % 2 == 0:
        y = Recursive_Power(a, b/2)
        return y * y % c
    else:
        y = Recursive_Power(a, (b-1)/2)
        return y * y * a % c

a, b, c = map(int, input().split())

print(Recursive_Power(a, b))