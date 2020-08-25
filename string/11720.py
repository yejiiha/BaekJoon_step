# Sum of number
n = int(input())
nth_num = list(map(int, input()))
sum = 0

for i in range(len(nth_num)):
    sum += nth_num[i]
print(sum)
