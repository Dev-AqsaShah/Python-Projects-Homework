days_in_year:int = 365
hours_per_day:int = 24
minutes_per_hour:int = 60
seconds_per_minute:int = 60

def seconds():
    print(f"There are {days_in_year * hours_per_day * minutes_per_hour * seconds_per_minute} seconds in a year")
    
if __name__ == "__main__":
    seconds()