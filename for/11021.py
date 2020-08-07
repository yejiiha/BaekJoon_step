# A+B-7
t = int(input())
list = []

for i in range(t):
    a, b = input().split()
    result = int(a) + int(b)
    list.append(result)

for n in range(t):
    print(f"Case #{n+1}: {list[n]}")
