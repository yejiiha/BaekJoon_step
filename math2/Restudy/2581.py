m = int(input())
n = int(input())

prime_list = []

for i in range(m, n+1):
    cnt = 0
    for j in range(1, i+1):
        if i%j ==0:
            cnt += 1
    if cnt == 2:
        prime_list.append(i)

if len(prime_list) != 0:
    print(sum(prime_list))
    print(min(prime_list))
else:
    print(-1)