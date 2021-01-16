## 정수 삼각형

import sys
input = sys.stdin.readline

n = int(input())
t = [list(map(int, input().split())) for _ in range(0, n)]

# for i in range(1, n):
#     for j in range(len(t[i])):
#         if j == 0:
#             t[i][j] += t[i-1][j]
#         elif j == i:
#             t[i][j] += t[i-1][j-1]
#         else:
#             t[i][j] += max(t[i-1][j], t[i-1][j-1])

# print(max(t[n-1]))

print(t)