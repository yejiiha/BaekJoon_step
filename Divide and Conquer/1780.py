## 종이의 개수

import sys

input = sys.stdin.readline

def cut_paper(x, y, n):
    global m_one, zero, p_one
    chk = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if(paper[i][j] != chk):
                for a in range(3):
                    for b in range(3):
                        cut_paper(x + a * n // 3, y + b * n // 3, n // 3)
                return
    # 모두 0일 때
    if chk == 0:
        zero += 1
        return
    # 모두 -1일 때
    elif chk == -1:
        m_one += 1
        return
    # 모두 1일 때
    else:
        p_one += 1
        return

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

m_one = 0
zero = 0
p_one = 0

cut_paper(0, 0, n)

print(m_one)
print(zero)
print(p_one)