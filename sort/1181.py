## 단어 정렬

n = int(input())
li = []

for _ in range(n):
    word = str(input())
    word_len = len(word)
    li.append((word, word_len))

li = list(set(li))
li.sort(key=lambda word:(word[1], word[0]))

for i in li:
    print(i[0])



