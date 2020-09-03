# a = []
# b = []

# for i in range(1, 10000001):
#     if i % 2 == 0:
#         # 짝수일 경우
#         a += [j for j in range(1, i+1)]
#         b += [j for j in range(i, 0, -1)]
#     else:
#         # 홀수일 경우
#         a += [j for j in range(i, 0, -1)]
#         b += [j for j in range(1, i+1)]

#     if len(a) >= x:
#         print(str(a[x-1])+'/'+str(b[x-1]))
#         break
X = int(input())

stage, key_X = 1, 1

while key_X + stage <= X:
    key_X += stage
    stage += 1

step = X - key_X
x, y = step + 1, stage - step

if stage % 2 == 0:
    print('{}/{}'.format(x, y))
else:
    print('{}/{}'.format(y, x))
