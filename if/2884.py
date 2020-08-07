# Alarm Clock
h, m = input().split()
h = int(h)
m = int(m)

if (0 <= h <= 23 and 0 <= m <= 59) and h > 0 and m < 45:
    print(h-1, m+15)
elif (0 <= h <= 23 and 0 <= m <= 59) and h == 0 and m < 45:
    print(23, m+15)
elif (0 <= h <= 23 and 0 <= m <= 59) and h > 0 and m > 45:
    print(h, m-45)
elif (0 <= h <= 23 and 0 <= m <= 59) and h == 0 and m > 45:
    print(h, m-45)
elif (0 <= h <= 23 and 0 <= m <= 59) and h > 0 and m == 45:
    print(h, m-45)
elif (0 <= h <= 23 and 0 <= m <= 59) and h == 0 and m == 45:
    print(h, m-45)
