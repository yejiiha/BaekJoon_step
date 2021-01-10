## 소트인사이드

import sys

n = int(sys.stdin.readline())

li = list(str(n))

reverse = list(reversed(sorted(li)))

for i in reverse:
    print(i, end="")
