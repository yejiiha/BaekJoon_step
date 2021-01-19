## 연속합

n = int(input())
a = list(map(int, input().split()))

li = [a[0]]

for i in range(len(a) - 1):
    li.append(max(li[i] + a[i + 1], a[i + 1]))

print(max(li))