## AC

import sys
from collections import deque

input = sys.stdin.readline
deq = deque()

def ac(com, li):
    left = True
    if len(li) < com.count('D'):
        return 'error'
    for c in com:
        if c == 'R': left = not left
        elif c == 'D':
            p = 0 if left else -1
            if li: li.pop(p)
            else: return 'error'
    if li:
        if left: return '[' + ','.join(li) + ']'
        else: return '[' + ','.join(reversed(li)) + ']'
    return '[]'

t = int(input())

for _ in range(t):
    p = input()
    n = int(input())

    li = input().rstrip()[1: -1].split(",")
    if (n == 0) or (n == '0') : li = []
    
    print(ac(p, li))
