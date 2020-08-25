word = input()
dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
sec = 0

for i in range(len(word)):
    for j in dial:
        if word[i] in j:
            sec += dial.index(j) + 3

print(sec)
