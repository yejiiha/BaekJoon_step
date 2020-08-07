# Print triangle of star("*") pattern in Python-2
n = int(input())

if(1 <= n <= 100):
    for i in range(n):
        print(" "*(n-i-1), end="")
        print("*"*(i+1))
