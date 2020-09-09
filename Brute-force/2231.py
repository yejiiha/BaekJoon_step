N = int(input())
n = 0


def get_sum_devided_num(x):
    devided_num = list(map(int, str(x)))
    sum_devided_num = x + sum(devided_num)

    return sum_devided_num


while get_sum_devided_num(n) != N:
    if n == N:
        n = 0
        break
    else:
        n += 1

print(n)
