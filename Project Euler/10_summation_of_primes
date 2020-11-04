def sieve(n):
    prim=[1]*(n-1)
    prim.insert(0,0)
    prim.insert(0,0)
    for i in range(2,n):
        if prim[i]==1:
            loop=2
            while loop*i<=n:
                prim[(loop*i)]=0
                loop+=1
    
    plist=[]
    for j in range(0,n+1):
        if prim[j]==1:
            plist.append(j)
    return sum(plist)
