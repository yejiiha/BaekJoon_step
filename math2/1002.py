t = int(input())

for _ in range(t):
    x_1, y_1, r_1, x_2, y_2, r_2 = map(int, input().split())

    r = ((x_1-x_2) ** 2 + (y_1 - y_2) ** 2) ** 0.5
    R = [r_1, r_2, r]

    m = max(R)
    R.remove(m)

    if r == 0 and r_1 == r_2:   # 두 원이 일치하는 경우
        print("-1")
    elif r == r_1 + r_2 or m == sum(R):   # 두 원이 외접 또는 내접하는 경우
        print("1")
    elif m > sum(R):    # 두 원이 만나지 않는 경우
        print("0")
    else:   # 두 원이 두 점에서 만나는 경우
        print("2")
