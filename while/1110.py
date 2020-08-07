# Cycle of sum
x = n = int(input())
cnt = 1

if not (0 <= int(n) <= 99):
    exit()

while True:
    ten = n // 10
    one = n % 10
    num = ten + one

    n = int(str(one) + str(num % 10))

    if(x == n):
        break
    else:
        cnt += 1

print(cnt)
