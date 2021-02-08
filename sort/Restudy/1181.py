## 단어 정렬

import sys
input = sys.stdin.readline

n = int(input())
word_li = []

for _ in range(n):
    word = str(input())
    word_len = len(word)
    word_li.append((word, word_len))

word_li = list(set(word_li))
word_li.sort(key = lambda x: (x[1], x[0]))

for i in word_li:
    print(i[0].rstrip())