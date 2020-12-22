t = int(input()) # 케이스 수

for i in range(t):
    k = int(input())  # 층
    n = int(input())  # 호수

    floor = [a for a in range(n+1)]

    for __ in range(k):
        for j in range(n):
            floor[j] += floor[j-1]

    print(floor[j-1])
        