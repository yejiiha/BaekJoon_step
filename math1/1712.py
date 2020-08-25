a, b, c = map(int, input().split())
x = 0

# while True:
#     total_income = c * x
#     total_price = a + (b*x)

#     if b >= c:
#         print(-1)
#     elif total_income > total_price:
#         print(x)
#         break
#     else:
#         x += 1

if b >= c:
    print(-1)
else:
    print(a//(c-b)+1)
