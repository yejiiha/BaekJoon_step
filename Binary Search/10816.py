## 숫자 카드 2

import sys
import time

input = sys.stdin.readline
start_time = time.time()

# def binary_search(i, N, start, end):
#     if start > end:
#         return 0

#     mid = (start + end) // 2

#     if i == N[mid]:
#        return N[start:end + 1].count(i)
#     elif i < N[mid]:
#         return binary_search(i, N, start, mid - 1)
#     else:
#         return binary_search(i, N, mid + 1, end)

# n = int(input())
# card = sorted(map(int, input().split()))
# m = int(input())
# num = map(int, input().split())

# num_dic = {}

# for i in card:
#     start = 0
#     end = n - 1
#     if i not in num_dic:
#         num_dic[i] = binary_search(i, card, start, end)

# print(' '.join(str(num_dic[x]) if x in num_dic else "0" for x in num ))

N = int(input())
arr_n = list(map(int,input().split()))
M = int(input())
arr_m = list(map(int,input().split()))

dic = dict()

for i in arr_n:
    try :
        dic[i] += 1
    except:
        dic[i] = 1

for i in arr_m:
    try:
        print(dic[i] , end = " ")
    except:
        print(0, end = " ")


print(time.time() - start_time)