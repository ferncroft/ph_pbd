import sys
import datetime

# Now we loop over lines in the system input
for line in sys.stdin:
    # Strip the line of whitespace and split into a list
    line = line.strip()
    details = line.split(',')
# add in morning, afternoon, evening, night
    tod = int(details[3][:2])
    if tod <= 12 and tod >= 7:
        tod = 'M'
    elif tod <= 16:
        tod = 'A'
    elif tod <= 20:
        tod = 'E'
    else:
        tod = 'N'
# add in day of week
    year, month, day = (int(x) for x in details[2].split('-'))    
    day = datetime.date(year, month, day).weekday()
    if day == 0:
        day = 'Monday'
    elif day == 1:
        day = 'Tuesday'
    elif day == 2:
        day = 'Wednesday'
    elif day == 3:
        day = 'Thursday'
    elif day == 4:
        day = 'Friday'
    elif day == 5:
        day = 'Saturday'
    elif day == 6:
        day = 'Sunday'
    else:
        day = 'Unknown'
    print(line + ',' + day + ',' + tod)

    
