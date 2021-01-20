## 연산자 끼워넣기

import sys
input = sys.stdin.readline

def expression(i, res, plus, minus, mul, div):
    global min_, max_
    if i == n:
        max_ = max(res, max_)
        min_ = min(res, max_)
        return
    
    else:
        if plus:
            expression(i + 1, res + a[i], plus - 1, minus, mul, div)
        if minus:
            expression(i + 1, res - a[i], plus, minus - 1, mul, div)
        if mul:
            expression(i + 1, res * a[i], plus, minus, mul - 1, div)
        if div:
            expression(i + 1,  -(-res // a[i]) if res < 0 else res // a[i], plus, minus, mul, div - 1)

n = int(input())
a = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

max_, min_ = -1000000001, 1000000001

expression(1, a[0], plus, minus, mul, div)
print(max_)
print(min_)

