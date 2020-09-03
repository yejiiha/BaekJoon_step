import sys
import math


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n / i == 1:
            break
        elif n % i == 0:
            return False
    return True


natural_li = list(range(2, 100001))
prime_li = []

for j in natural_li:
    if isPrime(j):

        prime_li.append(j)


for i in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    f_num = num // 2
    s_num = num // 2

    while f_num > 0:
        if f_num in prime_li and s_num in prime_li:
            if f_num + s_num == num:
                print(f_num, s_num)
                break
        f_num -= 1
        s_num += 1
