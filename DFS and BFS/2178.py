## 미로 탐색

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

matrix = [input().rstrip() for _ in range(n)]
visit = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = [[0, 0]]
visit[0][0] = 1

while queue:
    x, y = queue.pop(0)

    if x == n - 1 and y == m - 1:
        print(visit[x][y])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if visit[nx][ny] == 0 and matrix[nx][ny] == "1":
                visit[nx][ny] = visit[x][y] + 1
                queue.append([nx, ny])