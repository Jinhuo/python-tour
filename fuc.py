words = ['cat','window','defenetrate']
for w in words:
    print(w,len(w))
for x in words:
    if len(x) > 6 :
        words.insert(0,x)
        if len(words) > 6:
            break
print (words)