## 소인수분해

# [방법 1]
# n = int(input())

# i = 2

# while n != 1:
#     if n % i == 0:
#         n = n / i
#         print(i)
#     else:
#         i += 1

# [방법 2]
n = int(input())

for i in range(2, n + 1):
    while (n % i == 0):
        n /= i 
        print(i)
        i += 1