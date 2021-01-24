## 링

import sys

input = sys.stdin.readline

def gcd(x, y):
    while y:
        x, y = y, x % y

    return x

n = int(input())
r = list(map(int, input().split()))

for i in r[1:]:
    a = gcd(r[0], i)
    print(str(r[0] // a) + "/" + str(i // a))