from math import sqrt

while 1:
    n = int(input())
    cnt = 0

    if n == 0:
        break
    
    cnt = 0

    for i in range(n+1, 2*n+1):
        if i < 2:
            continue
        elif i == 2:
            cnt += 1
            continue
        else:
            for j in range(2, int(sqrt(i) + 1)):
                if i%j == 0:
                    break
            else:
                cnt += 1
    
    print(cnt)



