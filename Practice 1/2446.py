# Print triangle of star("*") pattern in Python-9
n = int(input())

if(1 <= n <= 100):
    for i in range(n):
        print(" "*i, end="")
        print("*" * (2*(n-i)-1))

    for i in range(n-2, -1, -1):
        print(" "*i, end="")
        print("*" * (2*(n-i)-1))
