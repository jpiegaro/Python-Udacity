def leapyr(a):
	if a%4 != 0:
		yr=0
	else:
		if a%100 != 0:
			yr=1
		else:
			if a%400 != 0:
				yr=0
			else:
				yr=1
	return yr

def daysMonth(month,year):
	yrres=leapyr(year)
	if month in {1,3,5,7,8,10,12}:
		return 31
	else:
		if month in {4,6,9,11}:
			return 30
		else:
			if yrres == 1:
				return 29
			return 28

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    fncday=daysMonth(month,year)
    if day < fncday:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False        

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days