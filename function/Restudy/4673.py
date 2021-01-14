## 셀프 넘버

def d(n):
    return n + sum(map(int, str(n)))

list = []
self_num_li = []

for i in range(10001):
    list.append(d(i))
    if i not in list:
        self_num_li.append(i)

for i in self_num_li:
    print(i)