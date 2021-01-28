## 색종이 만들기

import sys

input = sys.stdin.readline

def cut(x, y, n):
    global white, blue
    chk = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            # 하나라도 같은 색이 아니면
            if chk != paper[i][j]:
                # 1사분면
                cut(x, y, n // 2)
                # 2사분면
                cut(x, y + n // 2, n // 2)
                # 3사분면
                cut(x + n // 2, y, n // 2)
                # 4사분면
                cut(x + n // 2, y + n // 2, n // 2)
                return
    # 모두 흰색일 때
    if chk == 0:
        white += 1
        return
    # 모두 파란색일 때
    else:
        blue += 1
        return

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

white = 0
blue = 0

cut(0, 0, n)
print(white)
print(blue)
