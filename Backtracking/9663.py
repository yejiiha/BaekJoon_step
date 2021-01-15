## N-Queen

n = int(input())
ans = 0
a, b, c = [False] * n, [False] * (2*n -1), [False] * (2*n -1)

def queen(x):
    global ans
    if x == n:
        ans += 1
        return
    
    for y  in range(n):
        if (not a[y]  and not b[x+y] and not c[x-y+n-1]):
            a[y] = b[x+y] = c[x-y+n-1] = True
            queen(x+1)
            a[y] = b[x+y] = c[x-y+n-1] = False

queen(0)
print(ans)