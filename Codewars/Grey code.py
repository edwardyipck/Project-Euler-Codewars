from math import *

def mystery(n):
    if n<2:
        return n
    else:
        m = len(format(n,"b"))
        T = (2**(m-1))
        if n>=T:
            pos = -n + T -1
        else:
            pos = n + 1
        val = range(T)[pos]
        return T*(floor(n/T)) + mystery(val)
    
def mystery_inv(n):
    m = len(format(n,"b"))
    T = (2**(m-1))
    
    bin_n = str(format(n,"b"))
    nums = [int(b) for b in bin_n]

    for step,i in enumerate(nums):
        if step == 0:
            output = i*T
        else:
            if sum(nums[0:step])%2==0:
                output += i*(2**(m-1-step))
                print("a")
            else:
                output -= (i-1)*(2**(m-1-step))
                print("b")  
    return output