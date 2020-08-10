# Print average of the fabricated score
n = int(input())
x = list(map(int, input().split()))
m = max(x)
sum = 0

for i in range(n):
    x[i] = x[i] / m * 100
    sum += x[i]

print(sum / n)
