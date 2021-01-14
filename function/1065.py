# Get count of hansu
def is_han(num):  # 한수인지 아닌지 판별하는 함수
    x = list(map(int, num))
    if int(num) < 100:
        return True
    else:
        a = x[0]
        d = x[1] - a

        if(x[2]-x[1] == d):  # 등차수열이면
            return True
        else:
            return False


n = input()
count = 0

for i in range(1, int(n)+1):
    if is_han(str(i)) == True:
        count = count + 1
print(count)
