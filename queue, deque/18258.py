## 큐 2

import sys
from collections import deque

input = sys.stdin.readline
deq = deque()

def push(deq, x):
    deq.append(x)

def pop(deq):
    if not deq:
        return -1
    else:
        return deq.popleft()

def size():
    return len(deq)

def empty():
    return 0 if deq else 1

def front():
    if not deq:
        return -1
    else:
        return deq[0]

def back():
    if not deq:
        return -1
    else:
        return deq[-1]

n = int(input())

for _ in range(n):
    command = input().split()

    op = command[0]

    if op == "push":
        push(deq, command[1])
    elif op == "pop":
        print(pop(deq))
    elif op == "size":
        print(size())
    elif op == "empty":
        print(empty())
    elif op == "front":
        print(front())
    elif op == "back":
        print(back())