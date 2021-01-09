## 체스판 다시 칠하기

n, m = map(int, input().split())
square = [list(input()) for _ in range(n)]
num = []

for i in range(n-7):
    for j in range(m-7):
        w = 0
        b = 0
        for x in range(i, i + 8):
            for y in range(j, j + 8):  # 8X8 범위를 B와 W로 번갈아가면서 검사
                if (x + y) % 2 == 0:
                    if square[x][y] != "W" : w += 1
                    if square[x][y] != "B" : b += 1
                else:
                    if square[x][y] != "B" : w += 1
                    if square[x][y] != "W" : b += 1
        
        num.append(w)  # W로 시작했을 때 칠해야 할 부분
        num.append(b)  # B로 시작했을 때 칠해야 할 부분

print(min(num))  # 칠해야 하는 개수의 최소값