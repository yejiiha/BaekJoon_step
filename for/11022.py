# A+B-8
t = int(input())
list_sum = []
list_a = []
list_b = []

for i in range(t):
    a, b = input().split()
    a = int(a)
    b = int(b)
    list_a.append(a)
    list_b.append(b)
    result = a + b
    list_sum.append(result)

for n in range(t):
    print(f"Case #{n+1}: {list_a[n]} + {list_b[n]} = {list_sum[n]}")
