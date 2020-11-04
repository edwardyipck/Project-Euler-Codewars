import numpy as np
def snail(snail_map):
    a = np.array(snail_map)
    snail = []
    o = 1
    if snail_map == [[]]:
        return []
    while o !=0:
        #1
        if a.size != 1:
            for i in a[0]:
                snail.append(i)
            a = np.delete(a, 0, 0)
            print(a)
        else:
            o = 0  
            
        #2
        if a.size != 1:
            for i in a[:,-1]:
                snail.append(i)
            a = np.delete(a, -1, 1)
            print(a)
        else:
            o = 0 
        
        #3
        if a.size != 1:
            for i in a[-1,::-1]:
                print(i)
                snail.append(i)
            a = np.delete(a, -1, 0)
            print(a)
            
        else:
            o = 0 
        
        #4
        if a.size != 1:
            for i in np.flip(a[:,0],0):
                print(i)
                snail.append(i)
            a = np.delete(a, 0, 1)
            print(a)

        else:
            o = 0 
            
    snail.append(int(a[0]))
    
    return list(snail)
