def amount(n):
    for x in range((n//3)+1):
        for y in range((n//5)+1):
            if((3*x + 5*y) == n):
                return x+y
    return -1

n = int(input())
print(amount(n))
