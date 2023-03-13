def alphabet():
    chaine = 'abcdefghijklmnopqrstuvwxyz'
    i = 0
    while i <= len(chaine):
        print(chaine[:i])
        chaine = chaine[::]
        i += 1      
alphabet()