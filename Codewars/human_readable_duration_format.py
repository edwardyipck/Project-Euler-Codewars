def format_duration(seconds):
    WORDS = ("year","day","hour","minute","second")
    if seconds == 0:
        return "now"
    secs = int(seconds % 60)
    minutes = int(((seconds - secs) / 60) % 60)
    hours = int(((seconds - secs - 60*minutes) / 3600) % 24)
    days = int(((seconds - secs - 60*minutes - 60*60*hours) / 86400) % 365)
    years = int(((seconds - secs - 60*minutes - 60*60*hours - 24*60*60*days) / 31536000))
    
    times = (years,days,hours,minutes,secs)
    non_zero = sum(x > 0 for x in times)
    
    if non_zero == 1:
        for i in range(5):
            if times[i] !=0:
                output = str(times[i]) + " "+ str(WORDS[i])
                if times[i] != 1:
                    output+= "s"
                return output
            
    else:
        count = 0
        output = ""
        for i in range(5):
            if times[i] !=0:
                count+=1
                output += str(times[i]) + " "+ str(WORDS[i])
                if times[i] != 1:
                    output+= "s"
                if count == non_zero -1:
                    break
                output+= ", "
        
        for i in range(1,6):
            if times[-i] !=0:
                output += " and " + str(times[-i]) + " "+ str(WORDS[-i])
                if times[-i] != 1:
                    output+= "s"
                return output
