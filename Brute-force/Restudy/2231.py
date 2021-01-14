## 분해합

def divided_hap(n):
    return n + sum(map(int, str(n)))

n = int(input())
k = 0

while divided_hap(k) != n:
    if k == n:
        k = 0
    else:
        k += 1

print(k)