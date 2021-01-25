## 스택

import sys

input = sys.stdin.readline

def push(x):
    stack.append(x)

def pop():
    if not stack:
        return -1
    else:
        return stack.pop()

def size():
    return len(stack)

def empty():
    return 0 if stack else 1

def top():
    return stack[-1] if stack else -1

n = int(input())
stack = []

for _ in range(n):
    command = input().split()

    op = command[0]

    if op == "push":
        push(command[1])
    elif op == "pop":
        print(pop())
    elif op == "size":
        print(size())
    elif op == "empty":
        print(empty())
    elif op == "top":
        print(top())


