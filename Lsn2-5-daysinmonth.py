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

