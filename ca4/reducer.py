import sys
import datetime

def get_timeofday(tod):
    if tod <= 12 and tod >= 7:
        tod = 'M'
    elif tod <= 16:
        tod = 'A'
    elif tod <= 20:
        tod = 'E'
    else:
        tod = 'N'
    return tod

def get_dayofweek(dow):
    if dow == 1:
        dow = 'Monday'
    elif dow == 2:
        dow = 'Tuesday'
    elif dow == 3:
        dow = 'Wednesday'
    elif dow == 4:
        dow = 'Thursday'
    elif dow == 5:
        dow = 'Friday'
    elif dow == 6:
        dow = 'Saturday'
    elif dow == 7:
        dow = 'Sunday'
    else:
        dow = 'Unknown'
    return dow


# Now we loop over lines in the system input
for line in sys.stdin:
    # Strip the line of whitespace and split into a list
    line = line.strip()
    details = line.split(',')

    # add in morning, afternoon, evening, night
    tod = int(details[3][:2])
    tod = get_timeofday(tod)

    # add in day of week
    year, month, day = (int(x) for x in details[2].split('-'))    
    dow = datetime.date(year, month, day).isocalendar()[2]
    dow = get_dayofweek(dow)
    
    # add in week of year
    week = datetime.date(year, month, day).isocalendar()[1]
    
    # output result
    print(line + ',' + dow + ',' + tod + ',' + str(week))

    
