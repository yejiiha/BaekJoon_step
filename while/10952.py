# A+B-5
list = []

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    sum = a + b
    list.append(sum)

n = 0

while n <= len(list)-1:
    print(list[n])
    n = n + 1
