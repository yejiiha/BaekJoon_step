## ATM

import sys

input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))

hap = 0
time = 0

for i in list(sorted(p)):
    hap += i
    time += hap

print(time)