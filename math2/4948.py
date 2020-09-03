import sys
import math


def prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


li = list(range(2, 246912))
prime_li = []

for i in li:
    if prime(i):
        prime_li.append(i)


while(True):
    count = 0
    n = int(sys.stdin.readline())

    if n == 0:
        break

    for i in prime_li:
        if n < i <= 2*n:
            count += 1

    print(count)

# while True:
#  n = int(sys.stdin.readline())
#   res = 0

#    for i in range(n+1, 2*n+1):
#         count = 0
#         for j in range(1, i+1):
#             if i % j == 0:
#                 count += 1
#                 if count > 2:
#                     break
#         if count == 2:
#             res += 1

#     print(res)

#     if n == 0:
#         break
