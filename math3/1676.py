## 팩토리얼 0의 개수

def factorial(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result

n = int(input())
w = str(factorial(n))[::-1]

cnt = 0

for i in w:
    if i == "0":
        cnt += 1
    else:
        break

print(cnt)

