# Test Scores
a = int(input())

if 0 <= a <= 100 and 90 <= a <= 100:
    print("A")
elif 0 <= a <= 100 and 80 <= a < 90:
    print("B")
elif 0 <= a <= 100 and 70 <= a < 80:
    print("C")
elif 0 <= a <= 100 and 60 <= a < 70:
    print("D")
else:
    print("F")
