## 덱

import sys
from collections import deque

input = sys.stdin.readline
deq = deque()

def push_front(deq, x):
    deq.appendleft(x)

def push_back(deq, x):
    deq.append(x)

def pop_front(deq):
    if not deq:
        return -1
    else:
        return deq.popleft()

def pop_back(deq):
    if not deq:
        return -1
    else:
        return deq.pop()

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

    if op == "push_front":
        push_front(deq, command[1])
    elif op == "push_back":
        push_back(deq, command[1])
    elif op == "pop_front":
        print(pop_front(deq))
    elif op == "pop_back":
        print(pop_back(deq))
    elif op == "size":
        print(size())
    elif op == "empty":
        print(empty())
    elif op == "front":
        print(front())
    elif op == "back":
        print(back())