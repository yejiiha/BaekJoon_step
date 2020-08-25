word = input()
changed_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in changed_alpha:
    word = word.replace(i, '_')

print(len(word))
