def trianglepascal(n):
    l=[]
    l.append([1])
    l.append([1,1])
    for i in range(2,n+1):
            x=[]
            x.append([1])

    for j in range(0,i-1):
        x.append(l[i-1][j]+l[i-1][j+1])
    x.append(1)
    l.append(x)


    for k in l:
        print(k)
    

    
