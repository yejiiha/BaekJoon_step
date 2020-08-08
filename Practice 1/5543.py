# Print minimum price
price_list_burger = []
price_list_drink = []
price_list_set = []
sum = 0

for a in range(0, 3):
    a = int(input())
    if 100 <= a <= 2000:
        price_list_burger.append(a)

for b in range(0, 2):
    b = int(input())
    if 100 <= b <= 2000:
        price_list_drink.append(b)

for i in range(0, 3):
    price_list_set.append(price_list_burger[i] + price_list_drink[0] - 50)
    price_list_set.append(price_list_burger[i] + price_list_drink[1] - 50)

price_list_set.sort()

print(price_list_set[0])
