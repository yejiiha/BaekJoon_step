# Find an alphabet
s = input()
alphabet = map(chr, range(97, 123))

find_s = list(map(s.find, alphabet))

for i in range(len(find_s)):
    print(find_s[i], end=" ")
