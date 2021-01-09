## 블랙잭

n, m = map(int, input().split())
card_li = list(map(int, input().split()))

result = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if card_li[i] + card_li[j] + card_li[k] > m:
                continue
            else:
                result = max(result, card_li[i] + card_li[j] + card_li[k])

print(result)