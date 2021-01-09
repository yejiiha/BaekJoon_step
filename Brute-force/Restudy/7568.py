## 덩치

n = int(input())
body_li = []

for _ in range(n):
    x, y = map(int, input().split())
    body_li.append((x, y))

for i in body_li:
    rank = 1
    for j in body_li:
        if (i[0] != j[0]) & (i[1] != j[1]):
            if (i[0] < j[0]) & (i[1] < j[1]):
                rank += 1
                
    print(rank, end=" ")