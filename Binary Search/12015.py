## 가장 긴 증가하는 부분 수열 2

import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

arr = [0]

for i in range(n):
    start, end = 0, len(arr) - 1

    # a[i]보다 작거나 같은수중에 제일 큰거 위치 찾기
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] < a[i]:
            start = mid + 1
        else:
            end = mid - 1
    
    # 위치가 배열보다 크다면 넣어준다.
    if start >= len(arr):
        arr.append(a[i])
    # 해당 위치의 숫자를 바꿔준다.
    else:
        arr[start] = a[i]

print(len(arr) - 1)
