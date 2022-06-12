a = input()
abc ='abcdefghijklmnopqrstuvwxyz'
for i in abc:
    if i not in a:
        print(-1, end=' ')
    else:
        print(a.index(i), end=' ')
        
