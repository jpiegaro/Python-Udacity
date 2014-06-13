def leapyr(a):
	if a%4 != 0:
		yr='common year'
	else:
		if a%100 != 0:
			yr='leap year'
		else:
			if a%400 != 0:
				yr='common year'
			else:
				yr='leap year'
	return yr