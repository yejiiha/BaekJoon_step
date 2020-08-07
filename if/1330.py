# Compare with two number
a, b = input().split()
a = int(a)
b = int(b)

if -10000 <= a and b <= 10000 and a > b:
    print(">")
elif -10000 <= a and b <= 10000 and a < b:
    print("<")
elif -10000 <= a and b <= 10000 and a == b:
    print("==")
