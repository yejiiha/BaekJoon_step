# Print max and what is the max value?
list = []
for x in range(9):
    x = int(input())
    list.append(x)

print(max(list))

for a in range(len(list)):
    if list[a] == max(list):
        print(a+1)
