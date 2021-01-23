## 최소공배수

def gcd(x, y):
    while y:
        x, y = y, x % y

    return x

def lcm(x, y):
    return x * y // gcd(x, y)

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    print(lcm(a, b))