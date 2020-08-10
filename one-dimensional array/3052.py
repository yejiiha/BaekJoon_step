# Get remainder and print how many different values are present
list = []
for i in range(10):
    i = int(input())
    if 0 < i < 1000:
        list.append(i % 42)

list = set(list)  # A set doesn't have order and doesn't allow duplication

print(len(list))
