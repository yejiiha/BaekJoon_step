# A+B-4
list = []

while True:
    try:
        a, b = map(int, input().split())
        sum = a + b
        list.append(sum)
    except EOFError:
        break

n = 0

while n <= len(list)-1:
    print(list[n])
    n = n + 1
