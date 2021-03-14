## 바이러스

import sys

input = sys.stdin.readline

n = int(input())
pair = int(input())

matrix = [[0] * (n + 1) for _ in range(n + 1)]
visit = []

for _ in range(pair):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1

def dfs(v):
    visit.append(v)
    for i in range(1, n + 1):
        if (i not in visit) and (matrix[v][i] == 1):
            dfs(i)
    
    return (len(visit) - 1)

print(dfs(1))

