## 피보나치 수 5

def Fibonacci(i):
    if i < 2:
        return i
    else:
        return Fibonacci(i-1) + Fibonacci(i-2)

n = int(input())

print(Fibonacci(n))