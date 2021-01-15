## 파도반 수열

import sys

input = sys.stdin.readline
t = int(input())

arr = [int(input()) for _ in range(t)]
sequence = [1, 1, 1, 2, 2]

for i in range(5, max(arr)):
    sequence.append(sequence[i-1] + sequence[i-5])

for i in arr:
    print(sequence[i-1])

