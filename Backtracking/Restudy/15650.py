## n과 m (2)

n, m = map(int, input().split())

check = [0 for _ in range(n)]      # 중복숫자 체크
array = []                         # 출력할 수열
 
def back_tracking(x):
    if x == m:                     # 수열 m개를 충족할경우 출력
        print(*array)            
        return
            
    for i in range(n):
        if check[i] == 0:              
            check[i] = 1           # 중복 제거
            array.append(i + 1)

            back_tracking(x + 1)   # 다음 깊이 탐색
            array.pop()            # 탐사한 내용 제거

            for j in range(i + 1, n):
                check[j] = 0              

back_tracking(0)    