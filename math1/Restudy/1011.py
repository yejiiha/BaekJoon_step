import math
t = int(input()) # 테스트 케이스

for _ in range(t):
    x, y = map(int, input().split())
    d = int(y - x) # 거리

    if d <=3 :
        print(d)
    else:
        n = int(math.sqrt(d))
        print(n)

        if d == n**2:
            print(2*n-1)
        elif n**2 < d <= n**2 +n:
            print(2*n)
        else:
            print(2*n +1)


