## 수 정렬하기

n = int(input())
li = []
for _ in range(n):
    x = int(input())
    li.append(x)

for i in sorted(li):
    print(i)