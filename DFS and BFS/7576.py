## 토마토

from collections import deque
import sys

input = sys.stdin.readline

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

que = deque()

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            que.append([i, j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while que:
    x, y = que.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                que.append([nx, ny])

result = -2
check_cooked = 0

for i in matrix:
    for j in i:
        if j == 0:
            check_cooked = 1
        result = max(result, j)

if check_cooked:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1)