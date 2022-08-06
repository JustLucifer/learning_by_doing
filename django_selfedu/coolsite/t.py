word = input()
word = list(word)
for n, w in enumerate(word):
    if w.isupper():
        # w.lower()
        word.insert(n, f'_{w.lower()}')
        word.pop(n + 1)
print(''.join(word))