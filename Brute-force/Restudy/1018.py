## 체스판 다시 칠하기

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
square = []

for i in range(n - 7):
    for j in range(m - 7):
        w = 0
        b = 0
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if (x + y) % 2 == 0:
                    if board[x][y] != "W" : w += 1
                    if board[x][y] != "B" : b += 1
                else:
                    if board[x][y] != "B" : w += 1
                    if board[x][y] != "W" : b += 1

        square.append(w)
        square.append(b)


print(min(square))  # 칠해야 하는 개수의 최소값
