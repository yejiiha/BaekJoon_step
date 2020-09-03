from math import sqrt

t = int(input())
distance = []

for _ in range(t):
    x, y = map(int, input().split())
    distance.append(y-x)

for dis in distance:
    m = int(sqrt(dis))
    n = m + 1

    if m == 1:
        print(dis)
    elif dis >= m*n+1:
        print(m+n)
    elif dis >= m**2+1:
        print(m*2)
    else:
        print(m*2-1)
