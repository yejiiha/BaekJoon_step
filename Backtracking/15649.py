## N과 M (1)

n, m = map(int, input().split())

check = [False] * (n + 1)
result = [0 for _ in range(m)]

def sequence(index, n, m):
    if index == m:
        for i in range(m):
            print(result[i], end=" ")
        print()
        return
    
    for i in range(1, n + 1):
        if check[i]:
            continue
        result[index] = i
        check[i] = True
        sequence(index + 1, n, m)
        check[i] = False

sequence(0, n, m)