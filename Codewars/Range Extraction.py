def solution(args):
    output = []
    curr_range = []
    args = sorted(args)
    
    for i in range(len(args)):
        print(curr_range)
        if i == 0:
            if args[i]-args[i+1]==-1:
                curr_range.append(args[i])
            else:
                output.append(str(args[i]))
        
        elif args[i]-args[i-1]==1:
            curr_range.append(args[i])

        else:
            if not curr_range:
                curr_range.append(args[i])
            else:              
                if len(curr_range)<3:
                    for num in curr_range:
                        output.append(str(num))
                else:
                    output.append(str(str(curr_range[0])+"-"+str(curr_range[-1])))    
                curr_range = [args[i]]
                
    if curr_range:
        if len(curr_range)<3:
            for num in curr_range:
                output.append(str(num))
        else:
            output.append(str(str(curr_range[0])+"-"+str(curr_range[-1])))
        
    return ",".join(output)


print(solution([-80, -79, -78, -76, -74, -73, -70, -67, -65, -64, -61, -59, -56, -55, -52, -49, -47, -46, -45, -42, -39, -37]))