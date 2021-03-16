## 숨바꼭질

from collections import deque
import sys

input = sys.stdin.readline

def bfs():
    que = deque()
    que.append(n)

    while que:
        x = que.popleft()

        if x == k:
            print(dp[x])
            return

        for i in (x - 1, x + 1, x * 2):
            if 0 <= i < max and not dp[i]:
                dp[i] = dp[x] + 1
                que.append(i)

n, k = map(int, input().split())
max = 100001
dp = [0] * max
bfs()


