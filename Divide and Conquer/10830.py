## 행렬 제곱

def matrix_power(a, b):
    if b == 1:
        for i in range(n):
            for j in range(n):
                a[i][j] %= 1000
        return a
    elif b % 2 > 0:
        tmp = [[0 for _ in range(n)] for _ in range(n)]
        c = matrix_power(a, b-1)
        for i in range(n):
            for j in range(n):
                for b in range(n):
                    tmp[i][j] += c[i][b] * a[b][j]
                tmp[i][j] %= 1000
        return tmp
    else:
        tmp = [[0 for _ in range(n)] for _ in range(n)]
        c = matrix_power(a, b//2)
        for i in range(n):
            for j in range(n):
                for b in range(n):
                    tmp[i][j] += c[i][b] * c[b][j]
                tmp[i][j] %= 1000
        return tmp

n, b = map(int, input().split())

a = []

for _ in range(n):
    x = list(map(int, input().split()))
    a.append(x)

for i in matrix_power(a, b):
    for j in i:
        print(j, end = " ")
    print()