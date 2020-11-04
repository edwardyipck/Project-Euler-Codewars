def collatz(n):
    steplist=[]
    for i in range(2,n+1):
        steps=0
        while i!=1:
            if i % 2 ==0:
                i=i/2
                steps+=1
            else:
                i=3*i+1
                steps+=1
        steplist.append(steps)
    return (steplist.index(max(steplist))+2),max(steplistb)
