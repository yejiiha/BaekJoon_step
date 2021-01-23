## 약수

divisor_count = int(input())
divisor = list(map(int, input().split()))

divisor_max = max(divisor)
divisor_min = min(divisor)

print(divisor_max * divisor_min)