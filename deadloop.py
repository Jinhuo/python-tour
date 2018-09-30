words = ['cat','window','defenetrate']
words.insert(0,'dog')
print(words)
for w in words:
    if len(w) > 6:
        words.insert(0,w)
        if len(words) > 6:
            break
print(words)