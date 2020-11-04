def chain(n):
    from time import time
    start = time()
    dic={}
    count=0
    for i in range(1,568):
        stri=str(i)
        nums=[]
        for char in stri:
            nums.append(int(char))
        state=0
        curr=0
        
        while state!=1:
            curr=0
            for j in nums:
                curr+=j**2
            nums=[]
            stri=str(curr)
            for char in stri:
                nums.append(int(char))
            if curr==1:
                state=1
                dic[i]=0
            if curr==89:
                state=1
                dic[i]=1
                
    for j in range(1,n+1):
        strj=str(j)
        f=0
        for dig in strj:
            f+=int(dig)**2
        if dic[f]==1:
            count+=1
    print( "Time:", time() - start, "seconds.")
    return count
