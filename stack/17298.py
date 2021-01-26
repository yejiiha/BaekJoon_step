## 오큰수

n = int(input())
a = list(map(int, input().split()))
stack = []
nge = [-1] * n

for i in range(n):
    try:
        while a[stack[-1]] < a[i]:
            nge[stack.pop()] = a[i]
    except:
        pass

    stack.append(i)

for i in range(n):
    print(nge[i], end =" ")
