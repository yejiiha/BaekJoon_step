## 팩토리얼

def factorial(i):
    if i == 0:
        return 1
    return i * factorial(i - 1)

n = int(input())
print(factorial(n))