# Cumulative sum
n = int(input())
result = 0

if 1 <= n <= 10000:
    for i in range(1, n+1):
        result += i
    print(result)
