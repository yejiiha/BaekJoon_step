## N과 M (4)

# 방법 1
# n, m = map(int, input().split())

# check = [0] * (n + 1)
# result = [0] * m

# def backtracking(index, n, m):
#     if index == m:
#         for i in result:
#             print(i, end=" ")
#         print()
#         return
    
#     for i in range(1, n + 1):
#         if check[i]:
#             continue
#         result[index] = i
#         for j in range(i):  # i보다 작은 수는 모두 체크해줌
#             check[j] = 1
#         backtracking(index + 1, n, m)
#         for j in range(1, n + 1):  # 초기화
#             check[i] = 0

# backtracking(0, n, m)    

# 방법 2
n, m = map(int, input().split())
li = []

def backtracking(depth, idx, n, m):
    if depth == m:
        print(" ".join(map(str, li)))
        return
    
    for i in range(idx, n):
        li.append(i + 1)
        backtracking(depth + 1, i, n, m)
        li.pop()

backtracking(0, 0, n, m)

