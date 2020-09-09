n = int(input())

fibonacci_li = [0, 1]

for i in range(0, 20):
    fibonacci_li.insert(i+2, fibonacci_li[i+1] + fibonacci_li[i])

print(fibonacci_li[n])
