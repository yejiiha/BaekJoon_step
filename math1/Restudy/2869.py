a, b, v = map(int, input().split())

day = 1

while 1:
    day += 1
    if(a*day - b*(day-1) >=v):
        break


print(day)