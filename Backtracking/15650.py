## N과 M (2)

n, m = map(int, input().split())

check = [0] * (n + 1)
result = [0] * m

def sequence(index, n, m):
    if index == m:
        for i in range(m):
            print(result[i], end = " ")
        print()
        return
    
    for i in range(1, n + 1):
        if check[i]:
            continue
        result[index] = i   
        for j in range(i + 1):
            check[j] = 1
        sequence(index + 1, n, m)
        for j in range(1, i + 1):
            check[j] = 0
        
sequence(0, n, m)
print(check)

