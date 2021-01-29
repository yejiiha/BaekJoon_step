## 행렬 곱셈

n, m = map(int, input().split())

a = []
b = []

for _ in range(n):
    x = list(map(int, input().split()))
    a.append(x)

m, k = map(int, input().split())

for _ in range(m):
    x = list(map(int, input().split()))
    b.append(x)

c = [[0] * k for _ in range(n)]

for x in range(n):
    for y in range(k):
        for z in range(m):
            c[x][y] += a[x][z] * b[z][y] 

print(c)

for i in c:
    for j in i:
        print(j, end = " ")
    print()