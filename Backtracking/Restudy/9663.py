## N-Queen

n = int(input())

num = 0

a = [0] * n
b = [0] * (2*n - 1)
c = [0] * (2*n - 1)

def n_queen(i):
    global num
    if i == n:
        num += 1
        return
    
    for j in range(n):
        if not (a[j] or b[i + j] or c[i - j + n - 1]):
            a[j] = b[i + j] = c[i- j + n - 1] = 1
            n_queen(i + 1)
            a[j] = b[i + j] = c[i- j + n - 1] = 0

n_queen(0)
print(num)