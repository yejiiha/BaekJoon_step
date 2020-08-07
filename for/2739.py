# Say the multiplication tables.
n = int(input())

if 1 <= n <= 9:
    for i in range(1, 10):
        print(f"{n} * {i} = {n*i}")
else:
    print("1~9 범위의 정수를 입력하시오. ")
