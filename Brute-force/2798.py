n, m = map(int, input().split())
card_li = list(map(int, input().split()))
sum = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if card_li[i] + card_li[j] + card_li[k] > m:
                continue
            else:
                sum = max(sum, card_li[i] + card_li[j] + card_li[k])

print(sum)
