## 나이트의 이동

from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def bfs(sx, sy, ax, ay):
    que = deque()
    que.append([sx, sy])

    matrix[sx][sy] = 1

    while que:
        a, b = que.popleft()

        if a == ax and b == ay:
            print(matrix[ax][ay] -1)
            return 
            
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            
            if 0 <= nx < l and 0 <= ny < l and matrix[nx][ny] == 0:
                que.append([nx, ny])
                matrix[nx][ny] = matrix[a][b] + 1

t = int(input())

for _ in range(t):
    l = int(input())
    sx, sy = map(int, input().split()) # 나이트가 현재 있는 칸
    ax, ay = map(int, input().split()) # 나이트가 이동하려고 하는 칸
    
    matrix = [[0] * l for _ in range(l)]
    bfs(sx, sy, ax, ay)
