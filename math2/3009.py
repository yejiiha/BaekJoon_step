x_li = []
y_li = []
for i in range(0, 3):
    x, y = map(int, input().split())
    x_li.append(x)
    y_li.append(y)

for i in range(0, 3):
    if x_li.count(x_li[i]) == 1:
        x = x_li[i]
    if y_li.count(y_li[i]) == 1:
        y = y_li[i]

print(x, y)
