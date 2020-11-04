import numpy as np

def validSolution(board):
    check = set([1,2,3,4,5,6,7,8,9])
    x = np.array(board)
    
    if set(np.concatenate(x[:3,:3])) != check:
        return False
    if set(np.concatenate(x[3:6,:3])) != check:
        return False
    if set(np.concatenate(x[6:9,:3])) != check:
        return False
    if set(np.concatenate(x[:3,3:6])) != check:
        return False
    if set(np.concatenate(x[3:6,3:6])) != check:
        return False
    if set(np.concatenate(x[6:9,3:6])) != check:
        return False
    if set(np.concatenate(x[:3,6:9])) != check:
        return False
    if set(np.concatenate(x[3:6,6:9])) != check:
        return False
    if set(np.concatenate(x[6:9,6:9])) != check:
        return False
        
    for i in range(9):
        if set((x[i])) != check:
            return False
        if set((x[:,i])) != check:
            return False
        
    return True
