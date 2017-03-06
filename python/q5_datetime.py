# Hint:  use Google to find python function
from datetime import date
####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'

def date_difference(start_date, end_date):
  
	m1, d1, y1 = list(map(int, start_date.split('-')))
	m2, d2, y2 = list(map(int, end_date.split('-')))
  
	return (date(y2, m2, d2) - date(y1, m1, d1)).days

####b)
from datetime import date
date_start = '12312013'  
date_stop = '05282015'  

def date_difference2(start_date, end_date):
  
	m1, d1, y1 = int(start_date[:2]), int(start_date[2:4]), int(start_date[-4:])
	m2, d2, y2 = int(end_date[:2]), int(end_date[2:4]), int(end_date[-4:])

	return (date(y2, m2, d2) - date(y1, m1, d1)).days

####c)  
from datetime import date

date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'

def date_difference(start_date, end_date):
	months_str = ['Jan','Feb','Mar', 'Apr', 'May', 'Jun','Jul', 'Aug', 'Sep', 'Oct','Nov', 'Dec']
	months_int = list(range(1,12))
	t = list(zip(months_str, months_int))
	d = dict(t)
	d1, m1, y1 = list(start_date.split('-'))
	d2, m2, y2 = list(end_date.split('-'))
	m1 = d[m1]
	m2 = d[m2]

	return (date(int(y2), int(m2), int(d2)) - date(int(y1), int(m1), int(d1))).days
