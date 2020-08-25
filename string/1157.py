# count = {}
# word = list(input().upper())

# for i in word:
#     try:
#         count[i] += 1
#     except:
#         count[i] = 1

# print(count)

# for k, v in count.items():
#     if len(count) > 2 and v > 2:
#         print("?")
#         break
#     elif len(count) == 2 and v >= 2:
#         print(k)
#     elif len(count) == 1:
#         print(k)
#     elif len(count) > 1 and v == 1:
#         print(k, end="")

words = input().upper()
words_list = list(set(words))  # words에서 중복 제거하고 list에 넣기
word_count = list()  # word_list는 문자별 개수를 list에 넣은 것

for i in words_list:
    count = words.count(i)
    word_count.append(count)

print(word_count)

print(word_count.count(max(word_count)))

if(word_count.count(max(word_count)) >= 2):
    print('?')
else:
    print(words_list[(word_count.index(max(word_count)))])
