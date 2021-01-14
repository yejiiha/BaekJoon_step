## 한수

def hansu(n):
    if n < 100:
        return True
    else:
        h_li = list(map(int, str(n)))   
        if h_li[2] - h_li[1] == h_li[1] - h_li[0]:
            return True
        else: 
            return False

n = int(input())
cnt = 0

for i in range(1, int(n) + 1):
    if hansu(i) == True:
        cnt = cnt + 1
print(cnt)




