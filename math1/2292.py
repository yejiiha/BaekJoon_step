n = int(input())

cnt = 1
cnt_six = 6
count = 1

if n == 1:
    print("1")
else:
    while n > cnt:
        count += 1
        cnt += cnt_six
        cnt_six += 6

    print(count)
