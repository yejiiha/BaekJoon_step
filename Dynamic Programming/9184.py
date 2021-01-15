## 신나는 함수 실행
import sys 

def w(a, b, c):
    global result

    if (a, b, c) in result.keys():
        return result[(a, b, c)]

    if a <= 0 or b <= 0 or c <= 0 :
        return 1
    elif a > 20 or b > 20 or c > 20 :
        return w(20, 20, 20)

    elif a < b < c:
        result[(a, b, c)] =  w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return result[(a, b, c)]
    else:
        result[(a, b, c)] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
        return result[(a, b, c)]
    

while (1):
    a, b, c = map(int, sys.stdin.readline().split())
    result = dict()

    if a == -1 and b == -1 and c == -1:
        break
    
    print("w(%d, %d, %d) = %d" % (a, b, c, w(a, b, c)))
