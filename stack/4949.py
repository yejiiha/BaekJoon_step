## 균형잡힌 세상

while 1:
    s = input()
    stack = []
    temp = 1

    if s == ".":
        break

    for i in s:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")":
            if not stack or stack[-1] == "[":
                temp = 0
                break
            elif stack[-1] == "(":
                stack.pop()
        elif i == "]":
            if not stack or stack[-1] == "(":
                temp = 0
                break
            elif stack[-1] == "[":
                stack.pop()
    
    if temp == 1 and not stack:
        print("yes")
    else:
        print("no")




