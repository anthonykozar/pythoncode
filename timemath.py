import math

# Adds together a list of times represented as floating-point numbers:
# either minutes.seconds or hours.minutes
def sumtimes(times):
    minutes, seconds = (0,0)
    # convert each float to (WLOG) minutes & seconds
    for t in times:
        # get the fractional and integer parts of t
        f, i = math.modf(t)
        m = int(i)
        s = int(math.floor(f*100 + 0.5)) # convert 2 decimal places to int
        print m,s
        minutes += m
        seconds += s
    # convert seconds to minutes:seconds
    if seconds > 59:
        m, s = divmod(seconds, 60)
        minutes += m
        seconds = s
    return (minutes, seconds)
