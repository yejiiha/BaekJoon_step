## 별 찍기 - 10

def print_star(n):
    star_list = []
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            star_list.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            star_list.append(n[i % len(n)] * 3)
    return list(star_list)

n = int(input())
star = ["***", "* *", "***"]
cnt = 0

while n != 3:
    n = int(n / 3)
    cnt += 1

for i in range(cnt):
    star = print_star(star)

for i in star:
    print(i)