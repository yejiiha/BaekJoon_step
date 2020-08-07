# Print triangle of star("*") pattern in Python-1
n = int(input())

if(1 <= n <= 100):
    for i in range(n):
        for j in range(i+1):
            print("*", end='')
        print()
