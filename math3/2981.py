## 검문

import math

t = int(input())
n = [int(input()) for _ in range(t)]

if n[0] < n[1]:
    n_ = n[1] - n[0]
else:
    n_ = n[0] - n[1]

# 약수 구하기
n_divisor = [n_]

for i in range(2, int(math.sqrt(n_)) + 1):
    if n_ % i == 0:
        n_divisor.append(i)
        n_divisor.append(n_ // i)

# m 구하기
m = []

for i in range(len(n_divisor)):
    # 나머지 구하기
    r = n[0] % n_divisor[i]

    for j in range(1, len(n)):
        # 나머지 같은지 확인
        # 나머지가 다르면 패스
        if r != n[j] % n_divisor[i]:
            break
        # 모든 나머지가 같으면 m에 추가
        if j == len(n) - 1:
            m.append(n_divisor[i])

for i in sorted(m):
    print(i, end=" ")


