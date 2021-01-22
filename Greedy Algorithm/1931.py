## 회의실 배정

import sys

input = sys.stdin.readline

n = int(input())

meeting = []

for _ in range(n):
    start, end = map(int, input().split())
    meeting.append((start, end))

meeting = sorted(meeting, key = lambda a : (a[1], a[0]))

finish = 0
cnt = 0

for i, j in meeting:
    if i >= finish:
        cnt += 1
        finish = j

print(cnt)