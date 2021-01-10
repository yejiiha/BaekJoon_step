## 통계학
import sys
from collections import Counter

n = int(input())
num_li=[]

for _ in range(n):
    num_li.append(int(sys.stdin.readline()))

def mean(x):
    return round(sum(x) / len(x))

def median(x):
    return sorted(x)[len(x) // 2]

def mode(x):
    cnt = Counter(sorted(x))
    modes = cnt.most_common()    
    
    if len(x) > 1 : 
        if modes[0][1] == modes[1][1]:
            return modes[1][0]
        else : 
            return modes[0][0]
    else : 
        return modes[0][0]

def range(x):
    return max(x) - min(x)


print(mean(num_li))

print(median(num_li))

print(mode(num_li))

print(range(num_li))