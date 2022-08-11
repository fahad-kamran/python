for a in range (1,101,10):
    for b in range (a,a+10,1):
        if b<10:
            print('',b, end=' ')
        else:
            print(b, end=' ')
    print(' ')