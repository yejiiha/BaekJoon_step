# Print triangle of star("*") pattern in Python-21
n = int(input())
even = n // 2
odd = n - n // 2

if(1 <= n <= 100):
    for i in range(n):
        print("* " * odd)
        print(" *" * even)
