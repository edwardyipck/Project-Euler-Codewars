rules = {
    (0,0,0):0,
    (0,0,1):1,
    (0,1,0):1,
    (0,1,1):1,
    (1,0,0):1,
    (1,0,1):0,
    (1,1,0):0,
    (1,1,1):0
    }

def rule30(list_, n):
    if n<1:
        return list_
    
    for iter in range(n):
        output = []
        list_ = [0,0] + list_ + [0,0]
        for step in range(len(list_)):
            if step < len(list_)-2:
                look = tuple(list_[step:step+3])
                output.append(rules[look])
        list_ = output
    return output
                