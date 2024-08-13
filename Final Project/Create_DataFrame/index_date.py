import datetime


def index_date(today) : 
    # Get the current date and time
    now = today 


    # Print the year, month, and day of the current date
    year = now.year
    month = now.month
    day = now.day
    print(now.weekday())
    # Subtract one day from the current date
    if now.weekday() > 4 : 
        now = now - datetime.timedelta(days=1)
        if now.weekday() > 4 : 
            now = now - datetime.timedelta(days=1)
        

        now_str = f'{now.year}:{now.month}:{now.day}'
        now = now - datetime.timedelta(days=1)
    else :   
        now_str = f'{now.year}:{now.month}:{now.day}' 
        now = now - datetime.timedelta(days=1)
        
    return now_str,now

