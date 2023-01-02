def add_time(start='0:00', duration='0:00', day=None):

    # replace colon with space for the split
    start = start.replace(':', ' ')
    # split to separete hours, minutes and time of day
    start = start.split(' ')
    # get the starting data
    h_st = int(start[0]) # starting hour
    m_st = int(start[1]) # starting minute
    dtime_st = start[2] # starting time of day
    # check for 24 hour system
    if dtime_st == 'PM' and h_st != 12:
        h_st += 12

    # split the duration
    dur = duration.split(':')
    # get the duration data
    h_dur = int(dur[0]) # duration hour
    m_dur = int(dur[1]) # duration minute

    # turn the data into minutes
    mins_st = h_st*60 + m_st # starting minutes
    mins_dur = h_dur*60 + m_dur # duration minutes
    day_dur = 1440 # 24h day in minutes

    # get difference between the start and the end of a day
    diff = day_dur - mins_st 

    # calculating new time in minutes
    mins_res = mins_st + mins_dur

    # calculating the number of days passed and the ramaining minutes
    days_passed = mins_res // day_dur
    mins_rem = mins_res % day_dur

    # calculating new hours and minutes
    h_new = mins_rem // 60
    mins_new = mins_rem % 60

    # turning hours to the 12h system and for the output
    if h_new > 12:
        h_new -= 12
        dtime_new = 'PM'
    elif h_new == 12:
        dtime_new = 'PM'
    elif h_new == 0:
        h_new = 12
        dtime_new = 'AM'
    else:
        dtime_new = 'AM'

    # checking minutes for the output
    if mins_new < 10:
        mins_new = '0' + str(mins_new)

    # the output without the week day
    if day == None:
        # if the day is the same:
        if days_passed == 0:
            new_time = '{}:{} {}'.format(h_new, mins_new, dtime_new)
        # if it is the next day
        elif days_passed == 1:
            new_time = '{}:{} {} (next day)'.format(h_new, mins_new, dtime_new)
        # if several days passed
        else:
            new_time = '{}:{} {} ({} days later)'.format(h_new, mins_new, dtime_new, days_passed)
    
    # the output with the week day
    else:
        week = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday') # week tuple for the output
        day = day.lower() # turning to the lower case
        day_num = week.index(day) # current day number
        curr_day = lambda x: week[x].capitalize() # current day with the capital letter
        
        # if the day is the same:
        if days_passed == 0:
            new_time = '{}:{} {}, {}'.format(h_new, mins_new, dtime_new, curr_day(day_num))
        # if it is the next day
        elif days_passed == 1:
            day_num += 1
            if day_num == 7:
                day_num = 0
            new_time = '{}:{} {}, {} (next day)'.format(h_new, mins_new, dtime_new, curr_day(day_num))
        # if several days passed
        else:
            # calculating the day's number
            day_num += days_passed 
            # checking if it's in range
            if  (6 - day_num) >= 0:
                new_time = '{}:{} {}, {} ({} days later)'.format(h_new, mins_new, dtime_new, curr_day(day_num), days_passed)
            # if not, finding the excess
            else:
                day_num = day_num % 7 
                new_time = '{}:{} {}, {} ({} days later)'.format(h_new, mins_new, dtime_new, curr_day(day_num), days_passed)

    return new_time


week = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
for i in week:
    print(add_time("8:16 PM", "566:02", i))

# "6:18 AM, Monday (20 days later)"