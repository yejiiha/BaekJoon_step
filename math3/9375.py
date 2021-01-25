## 패션왕 신해빈

t = int(input())

for _ in range(t):
    n = int(input())
    wear = {}

    if n == 0:
        print(0)
        continue

    for __ in range(n):
        name, type = list(map(str, input().split()))

        if type in wear.keys():
            wear[type] += 1
        else:
            wear[type] = 1
    
    case = 1

    for i in wear.keys():
        case *= wear[i] + 1
    
    print(case - 1)





