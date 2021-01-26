## 스택 수열

n = int(input())

cnt = 1
stack = []
op = []
temp = 1

for _ in range(n):
    s = int(input())

    while cnt <= s:
        stack.append(cnt)
        op.append("+")
        cnt += 1
    
    if stack[-1] == s:
        stack.pop()
        op.append("-")
    else:
        temp = 0

if temp == 0:
    print("NO")
else:
    for i in op:
        print(i)