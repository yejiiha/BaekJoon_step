# self number
def d(n):
    return n + sum([int(i) for i in str(n)])


list1 = []
self_num_list = []

for i in list(range(1, 10001)):
    list1.append(d(i))
    if i not in list1:
        self_num_list.append(i)

for j in self_num_list:
    print(j)
