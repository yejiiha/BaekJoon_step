# Print the second largest number
list = []

a, b, c = map(int, input().split())

if (1 <= a <= 100) and (1 <= b <= 100) and (1 <= c <= 100):
    list.append(a)
    list.append(b)
    list.append(c)

list.sort()
print(list[1])
