n = int(input())
li = []

for _ in range(n):
    x, y = map(int, input().split())
    li.append((x, y))

for i in li:
    rank = 1
    for j in li:
        if (i[0] != j[0]) & (i[1] != j[1]):
            if (i[0] < j[0]) & (i[1] < j[1]):
                rank += 1

    print(rank, end=" ")
