# Print triangle of star("*") pattern in Python-13
n = int(input())

if (1 <= n <= 100):
    for i in range(n):
        for j in range(i+1):
            print("*", end='')
        print()
    for i in range(n-1):
        for j in range(n-1-i):
            print("*", end='')
        print()
