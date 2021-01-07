## 하노이 탑 이동 순서

n = int(input())
movement = []

def hanoi(n, a, b, c):
    if n == 1:
        movement.append((a, c))
    else:
        hanoi(n-1, a, c, b)
        movement.append((a, c))
        hanoi(n-1, b, a, c)

hanoi(n, 1, 2, 3)

print(len(movement))
for move in movement:
    print(move[0], move[1])