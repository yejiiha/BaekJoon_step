n = int(input())  # 단어의 개수
word_lst = []
cnt = 0

for i in range(n):
    word_lst = list(input())
    prev = word_lst.pop(0)
    # print(prev)

    word_set = set(prev)
    # print(word_set)
    is_group = True

    for j in word_lst:
        if j in word_set:
            if j != prev:  # 연속된 글자가 끝난 뒤 다시 글자가 등장했다면
                is_group = False
                break
        word_set.add(j)
        print(word_set)
        prev = j

    if is_group:
        cnt += 1

print(cnt)
