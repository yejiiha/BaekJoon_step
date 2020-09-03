t = int(input())  # 테스트 데이터 개수

for i in range(t):
    h, w, n = map(int, input().split())
    a = n % h  # 층
    b = n // h + 1  # 호수

    if a == 0:  # 가장 꼭대기 층에 머무는 경우
        a = h   # h층
        b -= 1  # n//h호수

    print(a*100 + b)
