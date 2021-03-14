## 유기농 배추

import sys

input = sys.stdin.readline

t = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = [[x, y]]
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 1:
                matrix[nx][ny] = 0
                queue.append([nx, ny])

for _ in range(t):
    m, n, k = map(int, input().split())
    matrix = [[0] * m for _ in range(n)]
    cnt = 0

    for __ in range(k):
        x, y = map(int, input().split())
        matrix[y][x] = 1
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                bfs(i, j)
                matrix[i][j] = 0
                cnt += 1
    print(cnt)

