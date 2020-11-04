def next_bigger(n):
    
    find = 0
    l = [str(x) for x in str(n)]
    s = len(l)
    for i in range(s-1):
        if int(l[-i-2]) < int(l[-i-1]):
            find = 1
            break       
    if find == 0:
        return -1

    right = l[-i-1:]
    right.sort()
    for j in range(len(right)):
        if right[j] > l[-i-2]:
            break
    swap = right[j]
    del right[j]
    right.append(l[-i-2])
    right.sort()
    left = l[:-i-2]
    final = str("".join(left))+str(swap)+str("".join(right))
    return int(final)
