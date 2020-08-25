num = list(input().split())
a = num[0]
b = num[1]

a_inverse = int(a[::-1])
b_inverse = int(b[::-1])

if a_inverse > b_inverse:
    print(a_inverse)
elif a_inverse < b_inverse:
    print(b_inverse)
