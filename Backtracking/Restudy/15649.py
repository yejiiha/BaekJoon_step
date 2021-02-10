## n과 m (1)

n, m = map(int, input().split())

num_li = [1 + i for i in range(n)]   # 숫자 리스트
check = [0] * n                      # 중복숫자 체크
array = []                           # 출력할 수열
 
def back_tracking(x):
    if x == m:                       # 수열 m개를 충족할경우 출력
        print(*array)            
        return
            
    for i in range(n):
        if check[i]:               # 중복될 경우 패스
            continue

        array.append(num_li[i])      # 수열 추가
        check[i] = 1            # 사용한 수 체크

        back_tracking(x + 1)                        # + 1번째 수열을 위해 재귀함수 호출

        array.pop()                       # 수열 마지막 자리 삭제
        check[i] = 0           # 사용한 수 초기화

back_tracking(0)    

