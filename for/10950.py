# A+B-3
t = int(input())
list = []

for i in range(t):
    a, b = input().split()
    result = int(a)+int(b)
    list.append(result)

for n in list:
    print(n)
