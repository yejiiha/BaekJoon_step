def stars(n):
    arr = []
    for i in range(3 * len(n)):
        if i // len(n) == 1:    # 가운데 큰 구멍
            arr.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            arr.append(n[i % len(n)] * 3)

    return(list(arr))


star = ["***", "* *", "***"]
n = int(input())
cnt = 0


while n != 3:
    n = int(n / 3)  # 가운데 작은 구멍
    cnt += 1

for i in range(cnt):
    star = stars(star)

for i in star:
    print(i)
