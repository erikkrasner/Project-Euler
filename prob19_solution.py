#!/usr/bin/env python
# 173
# 0.057s

def num_days(year,month):
    if month == 2:
	if year % 4 or (not year % 100 and year % 400):
	    return 28
	return 29
    if month in (4,6,9,11):
	return 30
    return 31

def first_of_month_sundays():
    first_of_month = 1
    num_sundays = 0
    for year in range(1901,2001):
	for month in range(1,13):
	    first_of_month += num_days(year,month)
	    first_of_month %= 7
	    if not first_of_month:
		num_sundays += 1
    return num_sundays

print first_of_month_sundays()
