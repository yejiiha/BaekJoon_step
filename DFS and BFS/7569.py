## 토마토 (2)

from collections import deque
import sys

input = sys.stdin.readline

m, n, h = map(int, input().split())
matrix = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

que = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if matrix[i][j][k] == 1:
                que.append([i, j, k])

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while que:
    z, x, y = que.popleft()

    for i in range(6):
        nz = z + dz[i]
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
            if matrix[nz][nx][ny] == 0:
                matrix[nz][nx][ny] = matrix[z][x][y] + 1
                que.append([nz, nx, ny])

result = -1
check_cooked = 1

for i in matrix:
    for j in i:
        for k in j:
            if k == 0:
                check_cooked = 0
            result = max(result, k)

if check_cooked == 0:
    print(-1)
elif result == 1:
    print(0)
else:
    print(result - 1)